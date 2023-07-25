import streamlit as st
import pandas as pd
import sys

sys.path.append('streamlit_website/check')

from check.spanish_word_freq import SpanishWordFreq
from check.word_chekcer import WordChecker

st.set_page_config(layout="wide", page_title="Buscar Palabra")

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
# Add css to make text bigger
st.markdown(
    """
    <style>
    write {
        font-size: 5rem !important;
    }
    input {
        font-size: 3rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
def load_words(file):
    word_data = pd.read_csv(file)
    word_data = word_data.drop(word_data.columns[0], axis=1)
    word_data.columns = ['Palabra', 'Tema', 'Video', 'Imagen', 'Sinómino']
    word_data.sort_values(by=['Palabra'])
    return word_data

with open("streamlit_website/css/style.css") as f:
    style = f.read()

with open("streamlit_website/css/bootstrap.css") as file:
    boot = file.read()

with open("streamlit_website/css/responsive.css") as file2:
    resp = file2.read()

st.write("")
st.header("Buscar Palabra")
word = st.text_input("Buscar Palabra", label_visibility="hidden")

word_data = load_words('/Users/celenap/streamlit_website/Search List2.csv')

word_list = word_data.loc[word_data['Palabra']==word]
word_data_no_acc = load_words('/Users/celenap/streamlit_website/Search List no acc.csv')
word_list_no_acc = word_data_no_acc.index[word_data_no_acc['Palabra']==word]

if not word_list.empty:
    table = word_list.to_html(classes='mystyle', escape=False, index=False)

    html_string = f'''

        <body>
            {table}
        </body>
        '''
    st.markdown(
            html_string,
        unsafe_allow_html=True)
    
elif not word_list_no_acc.empty:
    wl = word_data.iloc[word_list_no_acc[0]]['Palabra']
    word_list = word_data.loc[word_data['Palabra']==wl]
    table = word_list.to_html(classes='mystyle', escape=False, index=False)

    html_string = f'''

        <body>
            {table}
        </body>
        '''
    st.markdown(
            html_string,
        unsafe_allow_html=True)
    
if word_list.empty and word != "":
    filePath = "/Users/celenap/streamlit_website/pages/10000_frecuencias.txt"

    spanishWords = SpanishWordFreq(filePath)
    
    wordChecker = WordChecker(spanishWords.words, spanishWords.totalFreq)
         
    list = wordChecker.getCorrection(word.lower())

    st.write(f"La palabra {word} no exista en este diccionario")
    suggestions = ""
    for item in list:
        if item != word:
            suggestions += item + ' o '
    if suggestions[:-3] != "":
        st.write(f"¿Usted quiere buscar {suggestions[:-3]}?")
