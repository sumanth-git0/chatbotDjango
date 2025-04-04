import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=api_key)

def stt(filename):
    with open(filename, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=(filename, file.read()),
            model="whisper-large-v3",
            response_format="verbose_json",
        )
        return transcription.language,transcription.text

def translate(filename):
    with open(filename, "rb") as file:
        translation = client.audio.translations.create(
            model="whisper-large-v3",
            response_format="verbose_json",
            temperature=0.7,
            file=(filename, file.read()),
        )
        return translation

def tts(text,filepath):
    speech_file_path = filepath
    response = client.audio.speech.create(
        model="playai-tts",
        voice="Arista-PlayAI",
        input=text,
        response_format='wav',
    )
    return response.write_to_file(speech_file_path)

def response(query):
    messages = [
        {"role": "system","content": "You are a friendly and helpful assistant who always provides positive and supportive responses."},
        {"role": "user", "content": "Hello, how are you?"},
        {"role": "assistant", "content": "I'm doing well, thank you! How can I assist you today?"},
        {"role": "user", "content":query},
    ]
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.7,
        max_tokens=150,
    )
    return completion.choices[0].message.content

# audio_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audio_recordings', 'tel.m4a')
# filename = os.path.abspath(path=audio_file_path)
# stt(filename)
# translated_text = translate(filename,'te','hi').text
# response_text = response(translated_text)
# tts(response_text,'\\'.join(audio_file_path.split('\\')[:-1]))