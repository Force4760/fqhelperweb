from sidebar import sidebar
import streamlit as st
st.set_page_config(page_title='FQ Helper',layout = 'centered', initial_sidebar_state = 'collapsed')

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
sidebar()
