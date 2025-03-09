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

WILDFIRE_TEST_DIRECTORY = '/Users/ashmit/Documents/code/Projects/wildfire-detection/data/test/wildfire_low'
NO_WILDFIRE_TEST_DIRECTORY = '/Users/ashmit/Documents/code/Projects/wildfire-detection/data/test/not_wildfire_low'



wildfire_messages = []

print("wildfire predictions")
for i in os.listdir(WILDFIRE_TEST_DIRECTORY):
    img_path = f'{WILDFIRE_TEST_DIRECTORY}/{i}'
    encoded_img = encode_image(img_path)
    message = {
        "role": "user",
            "content": [
                {"type": "text", "text": "Tell me whether the following image is a wildfire or not. If wildfire return 1, if not return 0"},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{encoded_img}"}}
            ]
    }
    chat_completion = client.chat.completions.create(messages=[message], model="gpt-4o")
    print(chat_completion.choices[0].message.content, i)
    

not_wildfire_messages = []

print("not wildfire predictions")
for i in os.listdir(NO_WILDFIRE_TEST_DIRECTORY):
    img_path = f'{NO_WILDFIRE_TEST_DIRECTORY}/{i}'
    encode_image(img_path)
    encoded_img = encode_image(img_path)
    message = {
        "role": "user",
            "content": [
                {"type": "text", "text": "Tell me whether the following image is a fire or not. If it is a fire only return 1, if not only return 0"},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{encoded_img}"}}
            ]
    }
    chat_completion = client.chat.completions.create(messages=[message], model="gpt-4o")
    print(chat_completion.choices[0].message.content, i)
    

#chat_completion = client.chat.completions.create(messages=[not_wildfire_messages[0]], model="gpt-4o")
#print("nw", chat_completion)
