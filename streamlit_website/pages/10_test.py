import pandas as pd
import streamlit as st

# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")

chunksize = 5
TextFileReader = pd.read_csv('streamlit_website/Search List2.csv', chunksize=chunksize)

full_data = pd.concat(TextFileReader, ignore_index=True)

st.write(full_data.head(5))
