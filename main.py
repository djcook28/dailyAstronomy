import requests

image_url = 'https://api.nasa.gov/assets/img/general/apod.jpg'

image = requests.get(image_url)

with open('NASA image.jpg', 'wb') as img_file:
   img_file.write(image.content)