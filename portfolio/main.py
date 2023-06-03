import streamlit as st

st.set_page_config(layout='wide')
col1,col2=st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title("Amit Tambe")
    content = """
    
    Hi, I am Amit ! I am an QA Manager at private company. I graduated in 2008 from Pune University, India.
    I have worked with companies from various domain like health care, spend management.
    My Hobbies are travelling , exploring new places and foodies.
    """
    st.info(content)