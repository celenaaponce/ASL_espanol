import streamlit as st
from st_click_detector import click_detector
from time import sleep

placeholder = st.empty()
def render_content():
    content = """
    <a href='#' id='Image 1'><img width='20%' src='https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=200'></a>
    <a href='#' id='Image 2'><img width='20%' src='https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=200'></a>
    """
    with placeholder.container():
        clicked = click_detector(content, key='main')
    
    if clicked == 'Image 1':
        empty()
        with placeholder.container():
            clicked = click_detector(content, key='img1')
        st.header('First')
        st.write('here')

    elif clicked == 'Image 2':
        empty()
        with placeholder.container():
            clicked = click_detector(content, key='img2')
        st.header('Second')
        st.write('there')
        
def empty():
    placeholder.empty()
    sleep(0.01)
render_content()
