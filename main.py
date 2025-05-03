import streamlit
import getAPI
import downloadImage

api_key = 'YpFhAIDge6FkQLFW2dU9kFioWTDUXbbgVpoDVJg9'
api_url = 'https://api.nasa.gov/planetary/apod'

api_content = getAPI.getAPIContent(api_key, api_url)

downloadImage.download_image(api_content['url'])

print(api_content['title'])