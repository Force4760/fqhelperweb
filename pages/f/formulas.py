import streamlit as st
from pages.f.quantidade.quant import q
from pages.f.solucoes.solucoes import s
from pages.f.ondas.ondas import o
from pages.f.mecanica.mec import me
from pages.f.energia.energy import ene
form = ["Quantidade", "Soluções", "Energia", "Mecânica", "Ondas"]


def f():
    st.title("Fórmulas")
    f = st.selectbox("", form)
    if f == "Quantidade":
        q()
    elif f == "Soluções":
        s()
    elif f == "Ondas":
        o()
    elif f == "Mecânica":
        me()
    elif f == "Energia":
        ene()
    
    