# from googletrans import Translator
import requests
import os
from groq import Groq

# translator = Translator()

import pandas as pd

file_path = "translations.xlsx"
xls = pd.ExcelFile(file_path)
df = pd.read_excel(xls, sheet_name="Sheet1")

m,n = df.shape
src_languages = ['hi','te','ml']
for i in range(n):
    src_lan = src_languages[i]
    print(src_lan)
    for j in range(m):
        text = df.iloc[j,i]
        # translated_text = translator.translate(text, src=src_lan, dest="en")
        # print(translated_text.text)

        api_key = "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"
        api_url = "https://api.groq.com/v1/language/translate"

        llm = Groq(api_key=api_key)
        messages = [
            {"role": "user", "content": "Hello, how are you?"},
            {"role": "assistant", "content": "I'm doing well, thank you! How can I assist you today?"},
            {"role": "user", "content":f"recognize the language of text between backticks `{text}`, your response will be in the form 'text:text,language:language,translated_text: text translation into english' "},
        ]
        completion = llm.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
            max_tokens=150
        )
        print(type(completion.choices[0].message.content),end="\n")