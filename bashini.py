import requests

def bhashini_translate():
    url = "https://meity-auth.ulcacontrib.org/ulca/apis/v0/model/getModelsPipeline"
    headers = {
        "Authorization": "Bearer API_KEY",
        "Content-Type": "application/json"
    }
    # payload = {
    #     "text": text,
    #     "sourceLanguage": src_lan,
    #     "targetLanguage": trg_lan
    # }
    payload = {
        "inputData": {
            "audio":[],
            "input": [
                {
                    "source": "Hi"
                }
            ]
        },
        "pipelineTasks": [
            {
                "taskType": "asr",
                "config": {
                    "language": {
                        "sourceLanguage": "en"
                    }
                }
            },
            {
                "taskType": "translation",
                "config": {
                    "language": {
                        "sourceLanguage": "en",
                        "targetLanguage": "hi"
                    }
                }
            },
            {
                "taskType": "tts",
                "config": {
                    "language": {
                        "sourceLanguage": "hi"
                    }
                }
            }
        ],
        "pipelineRequestConfig": {
            "pipelineId" : "64392f96daac500b55c543cd"
        }
    }
    try:
        # files = {'audio': open('your_audio_file.wav', 'rb')}
        # response = requests.post(url, headers=headers, files=files)
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json().get("translatedText", "")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# text = "Hello, how are you?"

translated_text = bhashini_translate()
print("Bhashini Output:", translated_text)