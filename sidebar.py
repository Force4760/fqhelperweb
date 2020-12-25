import streamlit as st
from pages.c.converter import converter
from pages.ct.const_tables import table_const
from pages.s.sobre import s
def sidebar():
    sb = st.sidebar
    sb.title("FQ Helper")
    rad = sb.radio("", ["Constantes e Tabelas", "Fórmulas", "Conversor", "Sobre"])
    if rad == "Conversor":
        converter()
    elif rad == "Constantes e Tabelas":
        table_const()
    elif rad == "Sobre":
        s()
