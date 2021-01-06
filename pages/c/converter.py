import streamlit as st
from pages.c.functions import units, calc
tcon = ["Área", "Distância", "Energia", "Massa", "Potência", "Temperatura", "Tempo", "Velocidade", "Volume"]



def converter():
    st.title("Conversor")
    con = st.selectbox("", tcon)
    v = st.number_input(label='Valor', format="%g" , step=1.0)
    u1 = st.selectbox("De", units(con))
    u2 = st.selectbox("Para", units(con))
    st.title(f"{calc(v, u1, u2, con)} {u2}")