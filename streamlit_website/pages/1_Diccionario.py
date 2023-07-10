import streamlit as st
import streamlit.components.v1 as com
import base64
st.set_page_config(layout="wide", page_title="Diccionario")



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

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)   
file_ = open("streamlit_website/images/dictionary.png", "rb")
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

    <!-- dictionary section -->
    <section class="dictionary_section">
      <div class="container">
        <div class="row">
          <div class="col-md-6">
            <div class="dictionary_img-container">
              <img src="data:image/png;base64,{data_url}" alt="">
            </div>
          </div>
          <div class="col-md-6">
            <div class="dictionary_detail-box">
              <h3>
                Diccionario
              </h3>
              <p>
                Este diccionario es señas en la lengua de ASL, con videos.  
                Tambien tiene fotos, y voz español.
              </p>
              <div class="">
                <button class="call_to-btn btn_white-border" onclick="goTo('Diccionario Completo')">Diccionario Completo</button><br />
              </div>
              <div class="">
                <button class="call_to-btn btn_white-border" onclick="goTo('Diccionario por Letra')">Buscar por Letra</button><br />
              </div>
              <div class="">
                <button class="call_to-btn btn_white-border" onclick="goTo('Diccionario por Tema')">Buscar Tema</button><br />
              </div>
              <div class="">
                <button class="call_to-btn btn_white-border" onclick="goTo('Buscar Palabra')">Buscar Palabra</button><br />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>


    <!-- end dictionary section -->



  </div>

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
