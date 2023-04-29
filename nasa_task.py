import requests
import streamlit as st

# Prepare API key and API url
api_key = '7yyYV5a4rdhfTtEWtoSSBIe15Ic2b6dOT4I9TR7I'
url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'


# Get the request data as a dictionary
response = requests.get(url)
response_json = response.json()


# Extract the image title, url and explanation
title = response_json['title']
image_url = response_json['url']
explanation = response_json['explanation']

# Download the image
image_filepath = 'img.png'
response2 = requests.get(image_url)
with open(image_filepath, 'wb') as file:
    file.write(response2.content)


# Set the web page
st.set_page_config(layout='wide')
st.title(title)
st.image('img.png')
st.write(explanation)