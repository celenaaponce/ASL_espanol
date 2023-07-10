import streamlit as st
import base64
import pandas as pd
from pathlib import Path 
import os
import requests
import gdown

from st_click_detector import click_detector
alpha_num = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k',
             12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u',
             22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: 'otra'}

alpha_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
st.set_page_config(layout="wide", page_title="Diccionario Por Letra")

hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem; padding-left: 0rem;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

@st.cache_data
def load_words():


    url = 'https://drive.google.com/file/d/1bii0vusXl-640sgVhRK2NVj8XCZtGgDx/view?usp=sharing'
    path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]

    word_data = pd.read_csv(path)
    word_data = word_data.drop(word_data.columns[0], axis=1)
    # word_data.columns = ['Palabra', 'Tema', 'Video', 'Imagen', 'Sinómino']
    # word_data.sort_values(by=['Palabra'])
    return word_data

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid' width=150>".format(
      img_to_bytes(img_path)
    )
    return img_html
with open("streamlit_website/css/style.css") as f:
    style = f.read()

with open("streamlit_website/css/bootstrap.css") as file:
    boot = file.read()

with open("streamlit_website/css/responsive.css") as file2:
    resp = file2.read()

if 'letter' not in st.session_state:
   st.session_state.letter = ""

if 'offset' not in st.session_state:
   st.session_state.offset = 0

if 'prev_letter' not in st.session_state:
   st.session_state.prev_letter = -1

def set_start(i):
   st.session_state.letter = i

def set_offset(i):
   st.session_state.offset = i

def set_prev(i):
   st.session_state.prev_letter = i

def back_offset(i):
   st.session_state.offset = i - 20

def reset_start():
   set_start("")

other = img_to_html('streamlit_website/images/otra.png')
def images(size):
      content= f"""
         <br>
         <br>
         <a href='#' id='Image 1'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/a.gif'></a>
         <a href='#' id='Image 2'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/b.gif'></a>
         <a href='#' id='Image 3'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/c.gif'></a>
         <a href='#' id='Image 4'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/d.gif'></a>
         <a href='#' id='Image 5'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/e.gif'></a>
         <a href='#' id='Image 6'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/f.gif'></a>
         <a href='#' id='Image 7'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/g.gif'></a>
         <a href='#' id='Image 8'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/h.gif'></a>
         <a href='#' id='Image 9'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/i.gif'></a>
         <a href='#' id='Image 10'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/j.gif'></a>
         <a href='#' id='Image 11'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/k.gif'></a>
         <a href='#' id='Image 12'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/l.gif'></a>
         <a href='#' id='Image 13'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/m.gif'></a>
         <a href='#' id='Image 14'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/n.gif'></a>
         <a href='#' id='Image 15'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/o.gif'></a>
         <a href='#' id='Image 16'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/p.gif'></a>
         <a href='#' id='Image 17'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/q.gif'></a>
         <a href='#' id='Image 18'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/r.gif'></a>
         <a href='#' id='Image 19'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/s.gif'></a>
         <a href='#' id='Image 20'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/t.gif'></a>
         <a href='#' id='Image 21'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/u.gif'></a>
         <a href='#' id='Image 22'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/v.gif'></a>
         <a href='#' id='Image 23'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/w.gif'></a>
         <a href='#' id='Image 24'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/x.gif'></a>
         <a href='#' id='Image 25'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/y.gif'></a>
         <a href='#' id='Image 26'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/z.gif'></a>
         <a href='#' id='Image 27'>{other}</a>
         """
      clicked = click_detector(content)
      return clicked

clicked = images(10)
set_start(clicked[6:])

if clicked == "":
   pass

elif clicked[6:] == '27':
    set_prev(st.session_state.letter)
    word_data = load_words()
    st.write(word_data.head(5))
    # alpha_list = word_data[~word_data.Palabra.str.startswith(alpha_tuple)]
    # alpha_list.sort_values(by=['Palabra'])
    # max_len = len(alpha_list)
    # next_list = alpha_list[0:20]
    # table = next_list.to_html(classes='mystyle', escape=False, index=False)
    # html_string = f'''

    #     <body>
    #         {table}
    #     </body>
    #     '''
    # st.markdown(
    #         html_string,
    #     unsafe_allow_html=True)

elif st.session_state.prev_letter != st.session_state.letter:

    set_prev(st.session_state.letter)
    word_data = load_words()
    st.write(word_data.head(5))
    # letter = alpha_num[int(st.session_state.letter)]
    # alpha_list = word_data.loc[word_data['Palabra'].str.startswith(letter, na=False)]
    # alpha_list.sort_values(by=['Palabra'])
    # max_len = len(alpha_list)
    # next_list = alpha_list[0:20]
    # table = next_list.to_html(classes='mystyle', escape=False, index=False)
    # html_string = f'''

    #     <body>
    #         {table}
    #     </body>
    #     '''
    # st.markdown(
    #         html_string,
    #     unsafe_allow_html=True)
    # col1, col2, col3 = st.columns([1,1,1])
    # if st.session_state.offset < max_len:
    #     col3.button('Proximas Palabras', on_click=set_offset, args=[st.session_state.offset+20])

elif st.session_state.prev_letter == st.session_state.letter:
    word_data = load_words()
    st.write(word_data.head(5))
    # letter = alpha_num[int(st.session_state.letter)]
    # alpha_list = word_data.loc[word_data['Palabra'].str.startswith(letter, na=False)]
    # alpha_list.sort_values(by=['Palabra'])
    # max_len = len(alpha_list)
    # next_list = alpha_list[st.session_state.offset:st.session_state.offset+20]
    # table = next_list.to_html(classes='mystyle', escape=False, index=False)
    # html_string = f'''

    #     <body>
    #         {table}
    #     </body>
    #     '''
    # st.markdown(
    #         html_string,
    #     unsafe_allow_html=True)
    # col1, col2, col3 = st.columns([1,1,1])
    if st.session_state.offset+20 < max_len:
        col3.button('Proximas Palabras', on_click=set_offset, args=[st.session_state.offset+20])
    if st.session_state.offset >= 20:
        col1.button('Palabras Anteriores', on_click = back_offset, args=[st.session_state.offset])

