import pandas as pd
import  streamlit as st
import  time
st.title("Diabetic Data Base")
s=pd.read_csv("diabetics.csv")

with st.spinner("Code by rohith is on the way !! to get the data"):
    time.sleep(6)
st.write(s)