import requests

def download_image(image_url):
   image = requests.get(image_url)

   #wb mean write byte. This allows the program to accurately decipher the bytes as rgb values
   # rather than ASCII or Unicode text values avoiding possible error
   with open('NASA image.jpg', 'wb') as img_file:
      img_file.write(image.content)