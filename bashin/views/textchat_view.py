from rest_framework import generics, status
from rest_framework.response import Response

from bashin.models.textchat import TextChat
from bashin.serializers.textchat_serializer import TextChatSerializer


class TextChatView(generics.ListCreateAPIView):
    queryset = TextChat.objects.all()
    serializer_class = TextChatSerializer
    def get(self,request):
        textchats = TextChat.objects.all()
        serializer = TextChatSerializer(textchats, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        data = request.data
