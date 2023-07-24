import streamlit as st
from st_click_detector import click_detector
from time import sleep
import streamlit.components.v1 as com

def render_content(): 
    content = """ <div id='images'>
    <a href='#' id='Image 1'><img width='20%' src='https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=200'></a>
    <a href='#' id='Image 2'><img width='20%' src='https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=200'></a>
    </div>
    """
    
    clicked = click_detector(content, key='main')
    
    com.html("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Count Occurrences of ID</title>
        </head>
        <body>
            
            <div id="element1">Element 1</div>
            <div id="element2">Element 2</div>
            <div id="element1">Element 3</div>
            <div id="element3">Element 4</div>
            <div id="element1">Element 5</div>
        
            <script>
                // Function to count occurrences of an ID
                function countOccurrencesOfId(id) {
                    var elements = document.getElementsByTagName('*');
                    var count = 0;
        
                    for (var i = 0; i < elements.length; i++) {
                        if (elements[i].id === id) {
                            count++;
                        }
                    }
        
                    return count;
                }
        
                // Usage example:
                var idToSearch = "images";
                var occurrences = countOccurrencesOfId(idToSearch);
                console.log("Occurrences of ID '" + idToSearch + "': " + occurrences);
            </script>
        </body>
        </html>

    """, width=1000, height = 600, scrolling = True)

render_content()
