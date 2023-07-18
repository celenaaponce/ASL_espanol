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
    content2 = """<p><a href='#' id='Link 1'>First link</a></p>
    <p><a href='#' id='Link 2'>Second link</a></p>
    <a href='#' id='Image 1'><img width='20%' src='data:image/jpeg;base64,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'></a>
    <a href='#' id='Image 2'><img width='20%' src='https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=200'></a>
    """

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
            clicked = click_detector(content2, key = 'second')
            st.markdown(f"**{clicked} clicked**" if clicked != "" else "**No click**")
            st.write('here')

    elif clicked == 'Image 2':
        placeholder.empty()
        st.header('Third')
        st.write('here2')
if __name__ == "__main__":
    main()





