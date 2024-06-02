from openai import OpenAI
import os
from dotenv import load_dotenv
import requests
load_dotenv()

api_key = os.environ.get('OPENAI_API_KEY')
client = OpenAI()
client.api_key = os.environ.get('OPENAI_API_KEY')


def openai_gen(base64_image):

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }
    payload = {
    "model": "gpt-4o",
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": """
            Using javascript and react.js, create code that will generate a front end that looks like the users mock up along with proper routing and functionality. 
            Just return the code, nothing else, no formalilities, bash inputs, or how to create the react app. 
            But do label the which code goes into which file by using /*START_FILE: <filename>*/ at the start and  /*END_FILE: <filename>*/ at the end. Do not use ```jsx   
            or any illegal characters such as emojis like 😊
            """
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}",
                "detail": "low"
            }
            }
        ]
        }
    ],
    "max_tokens": 1000
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    print(response.json()['choices'][0]['message']['content'])
    return response.json()['choices'][0]['message']['content']
