import streamlit as st
import pandas as pd

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

st.info("Below you can find some of the apps I have built in Python. Feel free to contact me !")

col3,empty_col,col4=st.columns([1.5,0.5,1.5])

df=pd.read_csv('data.csv',sep=';')

with col3:
    for index,row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f'images/{row["image"]}')
        st.write(f"[Source Code]({row['url']})")
with col4:
    for index,row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f'images/{row["image"]}')
        st.write(f"[Source Code]({row['url']})")