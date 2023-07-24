import streamlit as st
from st_click_detector import click_detector
from time import sleep

placeholder = st.empty()
def render_content():
    content = """
    <div class = 'images'>
    <a href='#' id='Image 1'><img width='20%' src='https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=200'></a>
    <a href='#' id='Image 2'><img width='20%' src='https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=200'></a>
    </div>
    """

    clicked = click_detector(content, key='main')
    
    if clicked == 'Image 1':
        st.header('First')
        st.write('here')

    elif clicked == 'Image 2':
        st.header('Second')
        st.write('there')
        
    st.markdown("""<!DOCTYPE html>
    <html>
      <head>
        <title>JS Counter</title>
        <link rel="stylesheet" type="text/css" href="style.css">
      </head>
    
      <body onload="incrementCount(10)">
        <div class="main_container" id="id_main_container">
          <div class="container_inner" id="display_div_id">
          </div>
        </div>
      </body>
    </html>
    <script>
      var counter_list = [10,10000,10000];
      var str_counter_0 = counter_list[0];
      var str_counter_1 = counter_list[1];
      var str_counter_2 = counter_list[2];
      var display_str = "";
      var display_div = document.getElementById("images");
    
      function incrementCount(current_count){
        setInterval(function(){
          // clear count
          while (display_div.hasChildNodes()) {
              display_div.removeChild(display_div.lastChild);
          }
          str_counter_0++;
          if (str_counter_0 > 99) {
            str_counter_0 = 10; // reset count
            str_counter_1++;    // increase next count
          }
          if(str_counter_1>99999){
            str_counter_2++;
          }
          display_str = str_counter_2.toString() + str_counter_1.toString() + str_counter_0.toString();
          for (var i = 0; i < display_str.length; i++) {
            var new_span = document.createElement('span');
            new_span.className = 'num_tiles';
            new_span.innerText = display_str[i];
            display_div.appendChild(new_span);
          }
        },1000);
      }
    </script>""", unsafe_allow_html=True)
render_content()
