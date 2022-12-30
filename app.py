import openai
import urllib.request
from PIL import Image
import streamlit as st

def generate_image(api_key,image_description):
  openai.api_key = api_key
  img_response = openai.Image.create(
    prompt = image_description,
    n=1,
    size="512x512")
  

  img_url = img_response['data'][0]['url']

  urllib.request.urlretrieve(img_url, 'img.png')

  img = Image.open("img.png")
  
  return img

# Page logo
st.image('ai_logo.png', width=100)

# page title
st.title('Image Generation Tool')
# Add a text beneath the title
st.subheader('Created with ♥️ by Abdur Rahman, IIT Delhi')
st.write('For a useless🤡')

# text input box for image recognition
api_key = st.text_input('Your OpenAI API Auth Key')
img_description = st.text_input('Image Desription')

if st.button('Generate Image'):
    
    generated_img = generate_image(api_key,img_description)
    st.image(generated_img)
    
