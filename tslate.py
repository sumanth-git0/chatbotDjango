import os

from groq import Groq

api_key = "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"
# api_url = "https://api.groq.com/v1/language/translate"
client = Groq(api_key=api_key)
filename = os.path.dirname(__file__) + "/audio.m4a"

with open(filename, "rb") as file:
    transcription = client.audio.transcriptions.create(
      file=(filename, file.read()),
      model="whisper-large-v3",
      response_format="verbose_json",
    )
    print(transcription.text)
# completion = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     messages=[
#         {
#             "role": "user",
#             "content": "hi"
#         },
#         {
#             "role": "assistant",
#             "content": "It's nice to meet you. Is there something I can help you with, or would you like to chat?"
#         },
#         {
#             "role": "user",
#             "content": ""
#         }
#     ],
#     temperature=1,
#     max_completion_tokens=1024,
#     top_p=1,
#     stream=True,
#     stop=None,
# )
#
# for chunk in completion:
#     print(chunk.choices[0].delta.content or "", end="")
