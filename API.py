import os
from openai import OpenAI
import base64


client = OpenAI(
    api_key=os.environ.get('OPENAI_KEY') # run export OPENAI_KEY=<key> to store key in env
)

PATH = "/Users/ashmit/Documents/code/Projects/wildfire-detection/data/test/not_wildfire/non_fire.197.png"

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

encoded_img = encode_image(PATH)




chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Tell me whether the following image is a wildfire or not. Output 1 for wildfire, 0 for not."},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{encoded_img}"}}
            ]
        }
    ],
    model="gpt-4o",
)


print(chat_completion.choices[0].message.content)
