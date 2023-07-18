import streamlit as st
import pandas as pd
import gdown
from st_click_detector import click_detector

def download_csv(file_id, output_file):
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, output_file, quiet=False)
def main():
    st.header('placeholder')
    placeholder = st.empty()
    st.header('placeholder2')
    placeholder_2 = st.empty()
    content = """<p><a href='#' id='Link 1'>First link</a></p>
    <p><a href='#' id='Link 2'>Second link</a></p>
    <a href='#' id='Image 1'><img width='20%' src='https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=200'></a>
    <a href='#' id='Image 2'><img width='20%' src='https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=200'></a>
    """
    clicked = ""
    with placeholder.container():
        st.header('Main')
        clicked = click_detector(content, key='main')
        st.markdown(f"**{clicked} clicked**" if clicked != "" else "**No click**")
    placeholder_2.empty()
    if clicked == 'Image 1':
        placeholder.empty()
        placeholder_2.empty()
        with placeholder_2.container():
            st.header('Second')
            clicked = click_detector(content, key = 'second')
            st.markdown(f"**{clicked} clicked**" if clicked != "" else "**No click**")
            st.write('here')

    elif clicked == 'Image 2':
        placeholder.empty()
        st.header('Third')
        st.write('here2')
if __name__ == "__main__":
    main()





