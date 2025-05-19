# core/image_generator.py
import openai
import requests

def generate_image_from_prompt(prompt, output_path="generated/hula_dancer.png"):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']
    img_data = requests.get(image_url).content
    with open(output_path, 'wb') as handler:
        handler.write(img_data)
    return output_path
