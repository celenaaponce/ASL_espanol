import streamlit as st
import streamlit.components.v1 as com
import base64
st.set_page_config(layout="wide", page_title="Quien Soy")



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

with open("css/style.css") as f:
    style = f.read()

with open("css/bootstrap.css") as file:
    boot = file.read()

with open("css/responsive.css") as file2:
    resp = file2.read()

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)   
file_ = open("/Users/celenap/streamlit_website/images/celena2.jpeg", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
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

    <section class="about_me_section">
      <div class="container">
        <div class="row">
          <div class="col-md-6">
            <div class="about_me_detail-box">
              <h3>
                Sobre Yo
              </h3>
              <p>
                Me llamo Celena Ponce.  Crecí en Vancouver, WA.  Hablo español, lengua de señas americana e ingles.
                He trabajado con la comunidad sorda por 10 años.  He trabajado por Purple, una de las companias de 
                telefonos de video para personas Sordas.  Tambien tengo certificado como interprete de español en el 
                estado de Washington.  Enseño clases de lengua de señas americana en español para CDHY.
              </p>
              <h3>
                Información de Contacto
              </h3>
              <p>Número de Telefono: 360.521.2732 <br>
                Correo Electronico: celena.a.ponce@gmail.com <br>
                <a href = "mailto: celena.a.ponce@gmail.com">Mandar Mensaje</a>
              </p>
            </div>
          </div>
          <div class="col-md-6">
            <div class="about_me_img-container">
            <img src="data:image/jpg;base64,{data_url}" alt="">
            </div>
          </div>
        </div>
      </div>
    </section>


    <!-- end dictionary section -->



  </div>

</body>
""", width=1000, height = 450)