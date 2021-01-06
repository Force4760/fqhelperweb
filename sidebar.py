import streamlit as st
from pages.c.converter import converter
from pages.ct.const_tables import table_const
from pages.s.sobre import s
from pages.f.formulas import f

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
    elif rad == "Fórmulas":
        f()
