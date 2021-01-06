import streamlit as st
import webbrowser


ig = "https://www.instagram.com/force_4760/"
gh = "https://github.com/Force4760"

what = """  FQ Helper

   - FQ Helper web é uma web app com foco nos estudantes de Física e Química do 10º e 11º ano.
    
   - FQ Helper disponibilisa Conversores de unidades, Fórmulas e tabelas com constantes e valores imporatntes.
"""
def s():
    st.title("Sobre")
    st.subheader(what)
    st.header("Contacto")
    st.markdown(f" - [Instagram]({ig})")
    st.markdown(f" - [GitHub]({gh})")