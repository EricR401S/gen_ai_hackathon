from dotenv import load_dotenv
import openai
import os
import streamlit as st
import requests
from PIL import Image
from source.mask_image import masker

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(
    page_title="Facial Details",
    # give me all the possible icons
    page_icon="🎭",
    layout="wide"
    )
st.sidebar.header("Facial Details")
st.sidebar.write("Fill out the following form to update the previous sketch.")
st.title("Detail Facial Features")

st.sidebar.markdown(
    """
    ## Instructions
    1. Type in the text box to update more details of the sketch.
    2. Click the button to update the sketch.
    3. If you feel the image resembles even better now, move to the next page by clicking Final Details in the sidebar.
    """
)
    
def save_my_image(image_url, file_path = 'img/recent_img.png'):
    # Use requests to download the image
    # Write the image to a file in binary mode
    # Hint: You want to use a 'with' statement
    data = requests.get(image_url).content
    f = open('img/img.png','wb')
    f.write(data)
    f.close()
    return None

def update_image(image, mask, prompt):
    response = openai.Image.create_edit(
    image=open(image, "rb"),
    mask=open(mask, "rb"),
    prompt=prompt,
    n=1,
    size="512x512"
    )
    image_url = response['data'][0]['url']
    save_my_image(image_url)
    return image_url

def change_mask_format(mask_path):
    mask = Image.open(mask_path)
    mask = mask.convert('RGBA')
    mask = mask.convert('LA')
    mask = mask.convert('L')
    mask.save(mask_path)
    return None

def app():
    col_1, col_2 = st.columns(2)
    
    with col_1:

        col_x, col_y = st.columns(2)
        with col_x:
            prompt_hair = st.text_input('Hair', placeholder='color, length, .etc')
            prompt_facial_hair = st.text_input('Facial Hair', placeholder='beard, mustache, .etc')
            prompt_complexion = st.text_input('Complexion', placeholder='skin tone, .etc')
            image = Image.open('img/img.png')
            # st.image(image, caption="Image from previous iteration", use_column_width=True)
            # show the image with smaller width
            st.image(image, caption="Image from previous iteration", width=150)
        with col_y:
            prompt_demeanor = st.text_input('Demeanor', placeholder='intimidating, friendly, .etc')
            prompt_expression = st.text_input('Expression', placeholder='smiling, frowning, .etc')
            prompt_distinguishing_features = st.text_input('Distinguishing Features', placeholder='tattoos, scars, .etc')
            if st.button("Update Sketch"):
                dalle_prompt = f"""
                        Update the hair style to be {prompt_hair} and with {prompt_facial_hair} visible.
                        With a {prompt_complexion} complexion, and {prompt_demeanor} demeanor.
                        The expression they showed is {prompt_expression}, and they have {prompt_distinguishing_features}.
                    """
                
                with col_2:
                    st.text("")
                    st.text("The description is:")
                    st.write(dalle_prompt)
                    # eric call the mask function here, and make sure that you save the mask.png file in the img folder as mask.png
                    masker("img/img.png", "img/mask.png")
                    change_mask_format("mask.png")
                    st.image(update_image("img/img.png", "mask.png", dalle_prompt))





if __name__ == "__main__":
    app()