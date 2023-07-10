import streamlit as st
import streamlit.components.v1 as com
import base64
st.set_page_config(layout="wide")
hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem; padding-left: 0rem; padding-right: 0}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

with open("./style.css") as f:
    style = f.read()

with open("css/bootstrap.css") as file:
    boot = file.read()

with open("css/responsive.css") as file2:
    resp = file2.read()

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)   

remote_css("https://fonts.googleapis.com/css?family=Poppins:400,700|Raleway:400,600&display=swap")
remote_css("https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css")

def open_image(file_path):
    file_ = open(file_path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return data_url

banner = open_image("/Users/celenap/streamlit_website/images/Online world-cuate (2).png")
dictionary = open_image("/Users/celenap/streamlit_website/images/dictionary.png")
classes = open_image("/Users/celenap/streamlit_website/images/Online learning-rafiki.png")
books = open_image("/Users/celenap/streamlit_website/images/Absorbed in-pana.png")
resource = open_image("/Users/celenap/streamlit_website/images/Selecting team-pana.png")

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

com.html(f"""
         <head>
  <!-- Basic -->
  <meta charset="utf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <!-- Mobile Metas -->
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
  <!-- Site Metas -->
  <meta name="keywords" content="" />
  <meta name="description" content="" />
  <meta name="author" content="" />   
  <style>{style}</style>
  <style>{boot}</style>
  <style>{resp}</style>
  <title>Lengua de Señas Americana en Español</title>
  </head>
  <body>
  <section class="hero_section ">
      <div class="hero-container container">
        <div class="hero_detail-box">
          <h1>
            ¡Aprender Lengua de Señas Americana en Su Propia Idoma!
          </h1>
        </div>
        <div class="hero_img-container">
          <p>
            Para padres Latinos de niños Sordos, sé que hay muchos retos.  
            Hay bastante que aprender, no solo idioma, pero cultura y más.
            Mi meta es ayudar padres Latinos entender la lengua de señas americana,
            sin necesitar saber ingles.  Tambien, quiero ayudar encontrar los 
            recursos que necesitan para que sus hijos pueden tener exitó.
          </p>
          <div class="hero_sidebar">
            <img src="data:image/png;base64,{banner}" alt="" class="banner">
            <div class="hero_btn-continer">
            <button class="call_to-btn btn_white-border" onclick="goTo('Quien Soy')">Quién Soy</button>
            </div>

          </div>
          
        </div>
      </div>
    </section>
  </div>
  <!-- end header section -->

  <div class="common_style">

    <!-- dictionary section -->
    <section class="dictionary_section">
      <div class="container">
        <div class="row">
          <div class="col-md-6">
            <div class="dictionary_img-container">
              <img src="data:image/png;base64,{dictionary}" alt="">
            </div>
          </div>
          <div class="col-md-6">
            <div class="dictionary_detail-box">
              <h3>
                Diccionario
              </h3>
              <p>
                Buscar señas y frases en un diccionario de Español a ASL
              </p>
              <div class="">
                <button class="call_to-btn btn_white-border" onclick="goTo('Diccionario')">Diccionario</button><br />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>


    <!-- end dictionary section -->

    <!-- classes section -->
    <section class="classes_section">
      <div class="container">
        <div class="row">
          <div class="col-md-6">
            <div class="classes_detail-box">
              <h3>
                Clases
              </h3>
              <p>
                Tomar clases gratis en español para aprender lengua de señas americana.
              </p>
              <div class="">
              <button class="call_to-btn btn_white-border" onclick="goTo('Clases')">Aprender más</button>
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="classes_img-container">
              <img src="data:image/png;base64,{classes}" alt="">
            </div>
          </div>
        </div>
      </div>
    </section>



    <!-- end classes section -->

    <!-- libros section -->
    <section class="libros_section">
      <div class="container">
        <div class="row">
          <div class="col-md-6">
            <div class="libros_img-container">
              <img src="data:image/png;base64,{books}" alt="">
            </div>
          </div>
          <div class="col-md-6">
            <div class="libros_detail-box">
              <h3>
                Libros
              </h3>
              <p>
                Mirar videos de libros en español con ASL
              </p>
              <div class="">
              <button class="call_to-btn btn_white-border" onclick="goTo('Libros')">Leer</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>


    <!-- end libros section -->
    <!-- resources section -->
    <section class="resources_section">
      <div class="container">
        <div class="row">
          <div class="col-md-6">
            <div class="resources_detail-box">
              <h3>
                Recursos
              </h3>
              <p>
                Recursos para familias con hijos Sordos
              </p>
              <div class="">
              <button class="call_to-btn btn_white-border" onclick="goTo('Recursos')">Econtrar Recursos</button>
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="resources_img-container">
              <img src="data:image/png;base64,{resource}" alt="">
            </div>
          </div>
        </div>
      </div>
    </section>
    </body>
    <script>
    function goTo(page) {{
        page_links = parent.document.querySelectorAll('[data-testid="stSidebarNav"] ul li a')
        page_links.forEach((link) => {{
            if (link.text == page) {{
                link.click()
            }}
        }})
    }}
</script>
    """, width=1000, height = 600, scrolling = True)
