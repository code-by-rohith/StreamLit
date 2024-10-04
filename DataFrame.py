import pandas as pd
import streamlit as st
import time
import plotly.express as px

st.title("Diabetes Data Dashboard")
s = pd.read_csv("diabetics.csv")

with st.spinner("Loading !"):
    time.sleep(6)

st.write(s)

fig1 = px.histogram(s, x='Glucose', title="Distribution of Glucose Levels",
                    labels={'Glucose':'Glucose Levels'}, nbins=30, color_discrete_sequence=['#1f77b4'])
st.plotly_chart(fig1)

fig2 = px.scatter(s, x='Age', y='BMI', color='Outcome', title="BMI vs Age",
                  labels={'BMI': 'Body Mass Index', 'Age': 'Age (years)'},
                  color_continuous_scale=px.colors.sequential.Viridis)
st.plotly_chart(fig2)


fig3 = px.box(s, x='Outcome', y='BloodPressure', title="Blood Pressure by Outcome",
              labels={'Outcome': 'Diabetic Outcome', 'BloodPressure': 'Blood Pressure (mm Hg)'},
              color='Outcome')
st.plotly_chart(fig3)

correlation = s.corr()
fig4 = px.imshow(correlation, title="Correlation Heatmap of Features",
                 color_continuous_scale='RdBu_r', origin='lower')
st.plotly_chart(fig4)


st.success("Visualization Completed!")
