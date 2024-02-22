import base64
import requests
from auth_openai import getOpenAIkey

# OpenAI API Key
api_key = getOpenAIkey()

# Function to encode the image
def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode('utf-8')

def analyze_image(image_file):
    # Getting the base64 string
    base64_image = encode_image(image_file)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What’s in this image?"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 80
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    

    return response.json()

