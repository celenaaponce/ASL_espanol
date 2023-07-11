import streamlit as st
import streamlit.components.v1 as com
import base64
st.set_page_config(layout="wide", page_title="Libros")

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

def open_image(file_path):
    file_ = open(file_path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return data_url

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)   
banner = open_image("streamlit_website/images/Absorbed in-pana.png")
bailar = open_image("streamlit_website/images/books/jirafas no pueden bailar.jpg")
araña = open_image("streamlit_website/images/books/la arana muy ocupada.jpg")
conejo = open_image("streamlit_website/images/books/el libro de colores de coneja blanca.jpeg")
dinos = open_image("streamlit_website/images/books/como dan las buenas noches los dinosaurios.jpg")
remote_css("https://fonts.googleapis.com/css?family=Poppins:400,700|Raleway:400,600&display=swap")
remote_css("https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css")
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

<body class="sub_page">
  
  <div class="common_style">

    <!-- books section -->
    <section class="libros_section">
      <div class="container">
        <div class="row">
          <div class="col-md-6">
            <div class="libros_detail-box">
              <h3>
                Libros
              </h3>
              <p>
                Estes son libros en ASL, con voz español.
              </p>
            </div>
          </div>
          <div class="col-md-6">
            <div class="libros_detail-box">
             <img src="data:image/png;base64,{banner}" alt="" class="banner">
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-md-5">
            <div class="libros_detail-box">
              <div class="libros">
              <img src="data:image/jpg;base64,{bailar}" alt="">
                <a href="https://www.youtube.com/watch?v=cfetJAwPAho" class="call_to-btn btn_white-border" target="_blank">
                  Jirafas No Pueden Bailar
                </a> 
              </div>
            </div>
          </div>
          <div class="col-md-5">
            <div class="libros_detail-box">
              <div class="libros">
              <img src="data:image/jpg;base64,{araña}" alt="">
                <a href="https://www.youtube.com/watch?v=u37prsL9Rik" class="call_to-btn btn_white-border" target="_blank">
                  La Araña Muy Ocupada
                </a> 
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-md-5">
            <div class="libros_detail-box">
              <div class="libros">
              <img src="data:image/jpg;base64,{conejo}" alt="">
                <a href="https://www.youtube.com/watch?v=2qgjqhVc5Aw" class="call_to-btn btn_white-border" target="_blank">
                  El Libro de Colores de Coneja Blanca
                </a> 
              </div>
            </div>
          </div>
          <div class="col-md-5">
            <div class="libros_detail-box">
              <div class="libros">
              <img src="data:image/jpg;base64,{dinos}" alt="">
                <a href="https://www.youtube.com/watch?v=wQCkUbaZLQQ" class="call_to-btn btn_white-border" target="_blank">
                  Como Dan Las Buenas Noches Los Dinosaurios
                </a> 
              </div>
            </div>
          </div>
        </div>
        
      </div>
    </section>


    <!-- end dictionary section -->



  </div>

</body>
""", width=1000, height = 600, scrolling = True)
