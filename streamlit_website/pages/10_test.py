import streamlit as st
from st_click_detector import click_detector
from time import sleep
import streamlit.components.v1 as com

def render_content():  
    str_html = """
        <!DOCTYPE html>
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
          var display_div = document.getElementById("display_div_id");
        
          function incrementCount(current_count){
            setInterval(function(){
              // clear count
              while (display_div.hasChildNodes()) {
                  display_div.removeChild(display_div.lastChild);
              }
              str_counter_0++;
              if (str_counter_0 > 99) {
                str_counter_0 = 0; // reset count
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
        </script>
    """
    st.markdown(str_html, unsafe_allow_html=True)
render_content()
