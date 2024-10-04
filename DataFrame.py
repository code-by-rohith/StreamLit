import pandas as pd
import streamlit as st
import time
import plotly.express as px

# Title of the app
st.title("Diabetes Data Dashboard")

# Load the dataset
s = pd.read_csv("diabetics.csv")

# Add a spinner for a loading effect
with st.spinner("Code by Rohith is on the way to get the data..."):
    time.sleep(6)

# Display the dataset
st.write(s)

# Plotly visualizations

# 1. Histogram of Glucose Levels
fig1 = px.histogram(s, x='Glucose', title="Distribution of Glucose Levels",
                    labels={'Glucose':'Glucose Levels'}, nbins=30, color_discrete_sequence=['#1f77b4'])
st.plotly_chart(fig1)

# 2. Scatter Plot - BMI vs. Age
fig2 = px.scatter(s, x='Age', y='BMI', color='Outcome', title="BMI vs Age",
                  labels={'BMI': 'Body Mass Index', 'Age': 'Age (years)'},
                  color_continuous_scale=px.colors.sequential.Viridis)
st.plotly_chart(fig2)

# 3. Box Plot - Blood Pressure by Outcome
fig3 = px.box(s, x='Outcome', y='BloodPressure', title="Blood Pressure by Outcome",
              labels={'Outcome': 'Diabetic Outcome', 'BloodPressure': 'Blood Pressure (mm Hg)'},
              color='Outcome')
st.plotly_chart(fig3)

# 4. Correlation Heatmap
correlation = s.corr()
fig4 = px.imshow(correlation, title="Correlation Heatmap of Features",
                 color_continuous_scale='RdBu_r', origin='lower')
st.plotly_chart(fig4)

# Footer message
st.success("Visualization Completed!")
