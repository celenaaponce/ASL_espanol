import streamlit as st
import pandas as pd
import gdown

def download_csv(file_id, output_file):
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, output_file, quiet=False)
def main():
    st.title("CSV File Reader")

    # Input file ID and output file name
    file_id = st.text_input("Enter the file ID:")
    output_file = "output.csv"

    # Download the file
    if st.button("Download"):
        download_csv('1ynYsJEwmJEiCqfDEbTzvBDvHWHKNZeLG', 'Small Preview2.csv')
        st.success("File downloaded successfully!")

    # Read the CSV file
    if st.button("Read CSV"):
        try:
            csv_length = 0    
            for chunk in pd.read_csv(fileinput, names=['Palabra', 'Tema', 'Video', 'Imagen', 'Sinómino'], skiprows=skip, chunksize=10000):
                csv_length += chunk.count()
            st.write(csv_length )
        except FileNotFoundError:
            st.error("Please download the file first.")

if __name__ == "__main__":
    main()
