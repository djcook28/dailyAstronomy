import streamlit as st
from getAPI import getAPIContent
from downloadImage import downloadImage

api_key = 'YpFhAIDge6FkQLFW2dU9kFioWTDUXbbgVpoDVJg9'
api_url = 'https://api.nasa.gov/planetary/apod'

api_content = getAPIContent(api_key, api_url)

downloadImage(api_content['url'])

st.title(api_content['title'])
st.write(api_content['date'])
st.image('Nasa image.jpg')
st.write(api_content['explanation'])