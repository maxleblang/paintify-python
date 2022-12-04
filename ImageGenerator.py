import openai
import os
from dotenv import load_dotenv
from CoverImage import CoverImage
import random
import string

class ImageGenerator:
    """Initialize a ImageGenerator object and authenticate the OpenAI API"""
    def __init__(self) -> None:
        #authenticate openai account when initiated
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        #openai.Model.list()
        print("OpenAI authenticated")
    
    """Function that generates an image using Dall-E 2
    :param description: image description string
    returns: a CoverImage object of the generated image
    """
    def generate_image(self,description):
        #API call to generate image
        response = openai.Image.create(
            prompt=description,
            n=1,
            size="256x256"
        )
        #get url of generated image
        image_url = response['data'][0]['url']
        #generate random filename to save image under
        filename = ''.join(random.choices(string.ascii_lowercase, k=5))
        #create Image object from url
        return CoverImage(image_url,filename)