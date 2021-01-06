import streamlit as st
from pages.f.quantidade.densidade import densidade
from pages.f.quantidade.gp import gp
from pages.f.quantidade.nump import nump
from pages.f.quantidade.n2 import n
from pages.f.quantidade.vm import vm
quant = ["Densidade", "Grau de pureza", "Número de Partículas", "Quantidade", "Volume Molar"]
def q():
    cal = ["Densidade (g/cm³)", "Massa (g)", "Volume (cm³)"]
    cols = st.beta_columns(2)
    q = cols[0].selectbox("Fórmula", quant)
    if q == "Densidade":
        cal = ["Densidade (g/cm³)", "Massa (g)", "Volume (cm³)"]
        c = cols[1].selectbox("A Calcular", cal)
        densidade(c)
    elif q == "Grau de pureza":
        cal = ["Grau de pureza (%)", "Massa pura (g)", "Massa total (g)"]
        c = cols[1].selectbox("A Calcular", cal)
        gp(c)
    elif q == "Número de Partículas":
        cal = ["N de partículas", "Quantidade (mol)"]
        c = cols[1].selectbox("A Calcular", cal)
        nump(c)
    elif q == "Quantidade":
        cal = ["Quantidade (mol)", "Massa (g)", "Massa molar (g/mol)"]
        c = cols[1].selectbox("A Calcular", cal)
        n(c)
    elif q == "Volume Molar":
        cal = ["Volume molar (dm³/mol)","Volume (dm³)", "Quantidade (mol)"]
        c = cols[1].selectbox("A Calcular", cal)
        vm(c)