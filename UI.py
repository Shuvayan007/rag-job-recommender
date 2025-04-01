import streamlit as st

options = ['AI Engineer', 'Data Scientist', 'Data Analyst']
st.selectbox('Select Your Target Job Role', options, placeholder="Please select an option")

st.file_uploader('Upload Your Resume here', type= "pdf", accept_multiple_files = False)

st.text_area('About Your Current Job Role', max_chars=500, placeholder='Write about your current job role....')

st.button('Submit')