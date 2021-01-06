import streamlit as st
from pages.f.solucoes.cm import cm
from pages.f.solucoes.cn import cn
from pages.f.solucoes.wa import wa
from pages.f.solucoes.xa import xa
from pages.f.solucoes.mm import mm
from pages.f.solucoes.vv import vv
from pages.f.solucoes.ppmm import ppmm
from pages.f.solucoes.ppmv import ppmv
quant = ["Concentração mássica", "Concentração", "Fração mássica", "Fração molar", "% Massa/Massa", "% Volume/Volume", "PPM Massa/Massa", "PPM Volume/Volume"]
def s():
    cal = ["Concentração mássica (g/dm³)", "Massa (g)", "Volume (dm³)"]
    cols = st.beta_columns(2)
    q = cols[0].selectbox("Fórmula", quant)
    if q == "Concentração mássica":
        cal = ["Concentração mássica (g/dm³)", "Massa (g)", "Volume (dm³)"]
        c = cols[1].selectbox("A Calcular", cal)
        cm(c)
    elif q == "Concentração":
        cal = ["Concentração (mol/dm³)", "Quantidade (mol)", "Volume (dm³)"]
        c = cols[1].selectbox("A Calcular", cal)
        cn(c)
    elif q == "Fração mássica":
        cal = ["Fração mássica", "Massa da amostra (g)", "Massa total (g)"]
        c = cols[1].selectbox("A Calcular", cal)
        wa(c)
    elif q == "Fração molar":
        cal = ["Fração molar", "Quantidade da amostra (mol)", "Quantidade total (mol)"]
        c = cols[1].selectbox("A Calcular", cal)
        xa(c)
    elif q == "% Massa/Massa":
        cal = ["% Massa/Massa", "Massa do soluto (g)", "Massa da solução (g)"]
        c = cols[1].selectbox("A Calcular", cal)
        mm(c)
    elif q == "% Volume/Volume":
        cal = ["% Volume/Volume", "Volume do soluto (dm³)", "Volume da solução (dm³)"]
        c = cols[1].selectbox("A Calcular", cal)
        vv(c)
    elif q == "PPM Massa/Massa":
        cal = ["PPM Massa/Massa", "Massa do soluto (g)", "Massa da solução (g)"]
        c = cols[1].selectbox("A Calcular", cal)
        ppmm(c)
    elif q == "PPM Volume/Volume":
        cal = ["PPM Volume/Volume", "Volume do soluto (dm³)", "Volume da solução (dm³)"]
        c = cols[1].selectbox("A Calcular", cal)
        ppmv(c)
    