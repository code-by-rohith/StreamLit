import streamlit as st
import time

st.title("Welcome")
a = st.text_input("Enter the text")
st.warning("blocked")
if a:
    if "welcome" in a:
        st.success("Ok")
    else:
        st.warning("No")
st.info("welcome")
st.latex(r'''(vikas)^2=a^2+b^2+2ab''')
value=st.selectbox("pick your cource",["science","social","maths"],index=0)
if value=="science":
    st.warning("Done with science")
elif value=="maths":
    st.warning("Done with Maths")
else:
    st.warning("Done with social")
st.multiselect("Select the role",["Maths","Science","Social"])

st.file_uploader("Upload Your Video")

st.code("""import streamlit as st

st.title("Welcome")
a = st.text_input("Enter the text")
if a:
    if "welcome" in a:
        st.success("Ok")
    else:
        st.warning("No")
st.info("welcome")
st.latex(r'''(a+b)^2=a^2+b^2+2ab''')
value=st.selectbox("pick your cource",["science","social","maths"],index=0)
if value=="science":
    st.warning("Done with science")
elif value=="maths":
    st.warning("Done with Maths")
else:
    st.warning("Done with social")
st.multiselect("Select the role",["Maths","Science","Social"])

st.file_uploader("Upload Your Video")""",language='c')


st.color_picker("Pick A color")
st.progress(24)


with st.spinner("Wait Vika "):
    time.sleep(20)


st.code("range(50)",language='python')
