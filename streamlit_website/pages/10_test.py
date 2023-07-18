import streamlit as st
import pandas as pd
import gdown
from st_click_detector import click_detector

def empty():
    placeholder.empty()
    sleep(0.01)

def main():
    placeholder = st.empty()
    content = """<p><a href='#' id='Link 1'>First link</a></p>
    <p><a href='#' id='Link 2'>Second link</a></p>
    <a href='#' id='Image 1'><img width='20%' src='https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=200'></a>
    <a href='#' id='Image 2'><img width='20%' src='https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=200'></a>
    """
    empty()
    with placeholder.container():
        clicked = click_detector(content, key='main')
        
    if clicked == 'Image 1':
        st.header('Second')
        st.write('here')

    elif clicked == 'Image 2':
        st.header('Third')
        st.write('here2')
if __name__ == "__main__":
    main()





