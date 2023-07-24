import streamlit as st
from st_click_detector import click_detector
from time import sleep
import streamlit.components.v1 as com

def render_content(): 
    
    st.title("Clickable Images with IDs")

    # Define a list of image URLs and their corresponding IDs
    images = [
        {"id": "img1", "url": "https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=200"},
        {"id": "img2", "url": "https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=200"},
        {"id": "img3", "url": "https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=200"}
    ]

    # Display the images and make them clickable
    for img in images:
        image_url = img["url"]
        image_id = img["id"]
        st.write(f"Image ID: {image_id}")
        st.image(image_url, use_column_width=True, caption=f"Image {image_id}", output_format="JPEG")
        # Use st.button to create clickable buttons
        if st.button(f"Click Image {image_id}"):
            # When the button is clicked, display the image ID
            st.write(f"You clicked Image {image_id}")
render_content()
