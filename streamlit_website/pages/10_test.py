import streamlit as st
from st_click_detector import click_detector
from time import sleep
import streamlit.components.v1 as com
from pathlib import Path 
import base64
import gdown
import pandas as pd

def render_content(): 
    com.html("""<!DOCTYPE html>
        <html>
        <head>
            <title>Clickable Images with IDs</title>
        </head>
        <body>
            <!-- Clickable Image 1 -->
            <img src="https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=200" alt="Image 1" width="30" height="20" id="img1">
        
            <!-- Clickable Image 2 -->
            <img src="https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=200" alt="Image 2" width="30" height="20" id="img2">
        
            <!-- Clickable Image 3 -->
            <img src="https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=200" alt="Image 3" width="30" height="20" id="img3">
        
            <!-- Display the clicked image ID -->
            <p id="clickedImageID">'Image'</p>
        
            <script>
                // Function to handle image click event
                function handleImageClick(event) {
                    var clickedImage = event.target; // Get the clicked image element
                    var imageID = clickedImage.id;   // Get the ID of the clicked image
                    
                    // Update the "clickedImageID" element with the clicked image ID
                    document.getElementById('clickedImageID').innerText = print_list(word_data[~word_data.Palabra.str.startswith(alpha_tuple)][0:20]);
                }
        
                // Attach click event listeners to the images
                var images = document.querySelectorAll('img');
                images.forEach(function(image) {
                    image.addEventListener('click', handleImageClick);
                });
            </script>
        </body>
        </html>
    """)
    
##constants
alpha_num = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k',
             12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u',
             22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: 'otra'}

alpha_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

##page configs
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

with open("streamlit_website/css/style.css") as f:
    style = f.read()

with open("streamlit_website/css/bootstrap.css") as file:
    boot = file.read()

with open("streamlit_website/css/responsive.css") as file2:
    resp = file2.read()

#initialize states
if 'download' not in st.session_state:
   st.session_state.download = False
  
if 'letter' not in st.session_state:
   st.session_state.letter = ""

if 'offset' not in st.session_state:
   st.session_state.offset = 0

if 'prev_letter' not in st.session_state:
   st.session_state.prev_letter = -1

if 'count' not in st.session_state:
  st.session_state.count = 0
  
   
def download_csv(file_id, output_file):
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, output_file, quiet=False)
    st.session_state.download = True
  
@st.cache_data
def load_words():
  csv_length = 0    
  for chunk in pd.read_csv('Search List2.csv', names=['Palabra', 'Tema', 'Video', 'Imagen', 'Sinómino'], chunksize=10000, skiprows=1):
          data = pd.DataFrame(chunk)
  return data

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid' width=150>".format(
      img_to_bytes(img_path)
    )
    return img_html

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

def print_list(next_list):
    with placeholder_2.container():
      table = next_list.to_html(classes='mystyle', escape=False, index=False)
      html_string = f'''
  
          <body>
              {table}
          </body>
          '''
      st.markdown(
              html_string,
          unsafe_allow_html=True)
  

if st.session_state.download == False:
  download_csv('1bii0vusXl-640sgVhRK2NVj8XCZtGgDx', 'Search List2.csv')
word_data = load_words()

if st.session_state.letter == '27': 
    set_prev(st.session_state.letter)
    alpha_list = word_data[~word_data.Palabra.str.startswith(alpha_tuple)]
    alpha_list.sort_values(by=['Palabra'])
    max_len = len(alpha_list)
    next_list = alpha_list[0:20]
    print_list(next_list)

  
if st.session_state.letter != "":
  letter = alpha_num[int(st.session_state.letter)]
  alpha_list = word_data.loc[word_data['Palabra'].str.startswith(letter, na=False)]
  alpha_list.sort_values(by=['Palabra'])
  max_len = len(alpha_list)

  if st.session_state.prev_letter != st.session_state.letter:
    set_prev(st.session_state.letter)
    next_list = alpha_list[0:20]
    offset = st.session_state.offset

  if st.session_state.prev_letter == st.session_state.letter:
    next_list = alpha_list[st.session_state.offset:st.session_state.offset+20]
    offset = st.session_state.offset+20
  print_list(next_list)
  col1, col2, col3 = st.columns([1,1,1])
  if offset < max_len:
      col3.button('Proximas Palabras', on_click=set_offset, args=[st.session_state.offset+20])
  if st.session_state.offset >= 20:
      col1.button('Palabras Anteriores', on_click = back_offset, args=[st.session_state.offset])
      
render_content()
