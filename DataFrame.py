import pandas as pd
import  streamlit as st
st.title("Diabetic Data Base")
s=pd.read_csv("diabetics.csv")
st.write(s)