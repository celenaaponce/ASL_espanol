import streamlit as st
from st_click_detector import click_detector
from time import sleep
import streamlit.components.v1 as com

def render_content(): 
    
    com.html("""<!DOCTYPE html>
        <html>
        <head>
            <title>Clickable Images with IDs</title>
        </head>
        <body>
            <!-- Clickable Image 1 -->
            <img src="https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=200" alt="Image 1" width="300" height="200" id="img1">
        
            <!-- Clickable Image 2 -->
            <img src="https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=200" alt="Image 2" width="300" height="200" id="img2">
        
            <!-- Clickable Image 3 -->
            <img src="https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=200" alt="Image 3" width="300" height="200" id="img3">
        
            <!-- Display the clicked image ID -->
            <p id="clickedImageID"></p>
        
            <script>
                // Function to handle image click event
                function handleImageClick(event) {
                    var clickedImage = event.target; // Get the clicked image element
                    var imageID = clickedImage.id;   // Get the ID of the clicked image
                    
                    // Update the "clickedImageID" element with the clicked image ID
                    document.getElementById('clickedImageID').innerText = "Clicked Image ID: " + imageID;
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
    st.write(imageID)
render_content()
