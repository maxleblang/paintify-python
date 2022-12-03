import requests 
import base64
from PIL import Image

class CoverImage:

    def __init__(self,image_url,filename) -> None:
        #pull image from url
        #request image url
        r = requests.get(image_url)
        #save image as png
        if r.status_code:
            with open(f'pngs/{filename}.png','wb') as f:
                img_data = r.content
                #save image to png folder
                f.write(img_data)
                print('Image saved')
            #convert image to jpg format
            #open image in png format
            img_png = Image.open(f'pngs/{filename}.png')
            #The image object is used to save the image in jpg format
            img_png.save(f'jpgs/{filename}.jpg')
            #generate Base64 string
            with open(f'jpgs/{filename}.jpg', 'rb') as image:
                self.b64 = base64.b64encode(image.read()).decode("utf-8")
            

