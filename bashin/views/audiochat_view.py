import os

from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from rest_framework.parsers import MultiPartParser, FormParser

from bashin.models.audiochat import AudioChat
from bashin.models.textchat import TextChat
from bashin.serializers.audiochat_serializer import AudioChatSerializer
from service import stt, translate, response, tts


class AudioChatView(generics.ListCreateAPIView):
    queryset = AudioChat.objects.all()
    serializer_class = AudioChatSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get(self,request):
        audio_chats = AudioChat.objects.all()
        serializer = AudioChatSerializer(audio_chats, many=True)
        # return render(request, 'audio_chat.html',{'audio_chats': audio_chats})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        try:
            data = request.data
            user_audio = data.get('user_audio')
            if not user_audio:
                text_chats = TextChat.objects.all()
                return render(request, 'audio_chat.html',{'form':AudioForm,'texts':TextChat.objects.all()})
                # return Response({"error": "No audio file provided."}, status=status.HTTP_400_BAD_REQUEST)
            assistant_audio = data.get('assistant_audio') or user_audio.split('.')[0]+'_response.m4a'
            audio_chat = AudioChat.objects.create(user_audio=user_audio,assistant_audio=assistant_audio)

            audio_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..', 'media/audio_recordings', user_audio)
            filename = os.path.abspath(path=audio_file_path)

            input_language,input_text = stt(filename=filename)
            audio_chat.language = input_language
            audio_chat.save()

            translated_text = translate(filename).text
            response_text = response(translated_text)
            tts(response_text, os.path.abspath(path='\\'.join(audio_file_path.split('\\')[:-1] + [assistant_audio])))

            TextChat.objects.create(
                chat=audio_chat,
                input_text=input_text,
                translated_text=translated_text,
                response_text=response_text
            )
            return Response({
                "message": "Audio processed successfully",
                "assistant_audio_url": assistant_audio,
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return render(request, 'audio_chat.html',{'texts':TextChat.objects.all()})
            # return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)