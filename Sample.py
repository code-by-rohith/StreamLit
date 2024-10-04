import streamlit as st

# Title of the app
st.title('Streamlit Widgets')

# Radio buttons
radio_choice = st.radio('Choose an option:', ['Option 1', 'Option 2', 'Option 3'])
st.write(f'You selected: {radio_choice}')

# Checkbox
checkbox_state = st.checkbox('Check this box')
st.write(f'Checkbox is {"checked" if checkbox_state else "not checked"}')

# Selectbox
selectbox_choice = st.selectbox('Select an option:', ['A', 'B', 'C', 'D'])
st.write(f'Selected: {selectbox_choice}')

# Multi-select
multi_select_choice = st.multiselect('Select multiple options:', ['One', 'Two', 'Three', 'Four'])
st.write(f'Multi-selected: {multi_select_choice}')

# Slider
slider_value = st.slider('Select a value:', min_value=0, max_value=100, value=50)
st.write(f'Slider value: {slider_value}')

# Text input
text_input = st.text_input('Enter some text:')
st.write(f'You entered: {text_input}')

# Text area
text_area = st.text_area('Enter a long text:')
st.write(f'You entered: {text_area}')

# Number input
number_input = st.number_input('Enter a number:', min_value=0, max_value=100, value=10)
st.write(f'Number input: {number_input}')

# Date input1
date_input = st.date_input('Select a date:')
st.write(f'Selected date: {date_input}')

# Time input
time_input = st.time_input('Select a time:')
st.write(f'Selected time: {time_input}')

# File uploader
file = st.file_uploader('Upload a file')
if file is not None:
    st.write(f'File uploaded: {file.name}')

# Button
if st.button('Click Me'):
    st.write('Button clicked!')

# Progress bar
progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)

# Expander
with st.expander('Expand for more information'):
    st.write('Here is some additional information hidden in the expander.')

# Dataframe
import pandas as pd
df = pd.DataFrame({
    'Column A': [1, 2, 3, 4, 5],
    'Column B': ['A', 'B', 'C', 'D', 'E']
})
st.write('DataFrame:', df)

# Map
import numpy as np
import pydeck as pdk
map_data = pd.DataFrame({
    'lat': [37.7749, 34.0522, 40.7128],
    'lon': [-122.4194, -118.2437, -74.0060],
    'city': ['San Francisco', 'Los Angeles', 'New York']
})
st.write('Map of cities:')
st.pydeck_chart(pdk.Deck(
    initial_view_state=pdk.ViewState(
        latitude=37.7749,
        longitude=-122.4194,
        zoom=4
    ),
    layers=[pdk.Layer(
        'ScatterplotLayer',
        data=map_data,
        get_position=['lon', 'lat'],
        get_fill_color=[255, 0, 0, 140],
        get_radius=200000,
    )]
))

