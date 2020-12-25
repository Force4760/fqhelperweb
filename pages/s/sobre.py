import streamlit as st
import webbrowser


ig = "https://www.instagram.com/force_4760/"
gh = "https://github.com/Force4760"

what = """FQ Helper
FQ Helper web é uma web app com foco nos estudantes de Física e Química do 10º e 11º ano.
FQ Helper disponibilisa Conversores de unidades, Fórmulas e tabelas com constantes e valores imporatntes.
"""
def s():
    st.title("Sobre")
    st.subheader(what)
    if st.button("Instagram"):
        webbrowser.open_new_tab(ig)
    if st.button("GitHub"):
        webbrowser.open_new_tab(gh)