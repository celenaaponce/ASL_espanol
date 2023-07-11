import pandas as pd
import streamlit as st
import io
import dropbox
DBX = dropbox.Dropbox(st.secrets["token"])
_, res = DBX.files_download("/Themes2.csv")

with io.BytesIO(res.content) as stream:
    df = pd.read_csv(stream, index_col=0)

st.write(df.head(5))
# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])




