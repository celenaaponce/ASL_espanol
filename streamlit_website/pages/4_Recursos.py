import streamlit as st
import streamlit.components.v1 as com
import base64
st.set_page_config(layout="wide", page_title="Recursos")



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
file_ = open("/Users/celenap/streamlit_website/images/Selecting team-pana.png", "rb")
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

      <section class="resources_section">
    <div class="container">
      <div class="row">
        <div class="col-md-6">
          <div class="resources_detail-box">
            <h2>
              Recursos
            </h2>
            <h3>Manos y Voces</h3>
              <p>
                <a href="https://www.facebook.com/groups/manosyvoces" target="_blank">Manos y Voces</a> está dedicada a ayudar a las familias con niños sordos
                o con dificultades auditivas, de manera imparcial respecto a modos o metodologías de comunicación.
              </p>
            <h3>Escuelas para los Sordos</h3>
              <p>
                <a href="https://www.asd-1817.org/deaf-schools" target="_blank">Escuelas para los Sordos</a> son escuelas de varias niveles, kinder al 12 grado.
                Algunos son publicos.  Los que son publicos son gratis y algunos tienen dormitorios donde niños pueden quedar si no viven cerca.
                Es un lugar buenisimo para niños sordos aprender más de su cultura y su idioma.
              </p>
            <h3>Centros para Sordos</h3>
              <p>
                <a href="https://www.nad.org/resources/directories/state-agencies-of-deaf-hoh/" target="_blank">Centros para Sordos</a> son lugares que ayudan
                personas sordos encontrar recursos de cualquier tipo.  Algunos tambien tienen actividades o otros servicios.
              </p>
            <h3>Council de Manos</h3>
              <p>
                <a href="https://www.facebook.com/councildemanos" target="_blank">Council de Manos</a> es una organización sin ánimo de lucro para 
                la comunidad latinx sorda, originalmente se llamaba Consejo Nacional de Sordos y Hipoacúsicos Hispano; “NCDHH”.
              </p>
          </div>
        </div>
        <div class="col-md-6">
          <div class="resources_img-box">
            <img src="data:image/png;base64,{data_url}" alt="">
          </div>
        </div>
      </div>
    </div>
  </section>

    <!-- end resources section -->



  </div>

</body>
""", width=1000, height = 600, scrolling = True)