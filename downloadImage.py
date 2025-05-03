import requests

def download_image(image_url):
   image = requests.get(image_url)

   with open('NASA image.jpg', 'wb') as img_file:
      img_file.write(image.content)