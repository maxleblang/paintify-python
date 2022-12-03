import openai
import os
from dotenv import load_dotenv
from CoverImage import CoverImage

class ImageGenerator:

    def __init__(self) -> None:
        #authenticate openai account when initiated
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        #openai.Model.list()
        print("OpenAI authenticated")
    
    def generate_image(self,description: str):
        #API call to generate image
        response = openai.Image.create(
            prompt=description,
            n=1,
            size="256x256"
        )
        #get url of generated image
        image_url = response['data'][0]['url']
        #create Image object from url
        return CoverImage(image_url,'test')