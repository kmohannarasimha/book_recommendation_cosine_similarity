import streamlit as st
import base64
st.image("ineuron logo.jpg",width=150)
st.markdown("# About ")
st.header('Decreption of the project:')
st.caption('The book recommendation system which can recommend users books based on their interested genres is a powerful tool that helps readers find books they will enjoy based on their preferences. The system uses machine learning algorithms to analyze the genre. It then recommends books to readers based on their preferred genre, making it easier for readers to discover new books they will enjoy.The system is designed to be user-friendly, with a simple interface that allows readers to select their preferred book and receive personalized recommendations. ')
st.header('Team members')
col1,col2,col3 = st.columns(3)
with col1:
    st.subheader("Mohan Narasimha")
    st.text('Computer Science and Engineering')
    st.text('vel Tech Chennai,India ')
    st.text('vtu14855@veltech.edu.in') 
    st.image("mohan.jpg",width=100)

with col2:
    st.subheader('Sindhu')
    st.text('Computer Science and Engineering')
    st.text('vel Tech Chennai,India ')
    st.text('vtu14858@veltech.edu.in')
    st.image("sindhu.jpg",width=100)
with col3:
    st.subheader('Vinila')
    st.text('Computer Science and Engineering')
    st.text('vel Tech Chennai,India ')
    st.text('vtu13641@veltech.edu.in')
    st.image("vinila.jpg",width=100)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('aboutbg.jpeg')
