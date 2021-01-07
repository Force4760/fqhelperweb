import streamlit as st
from pages.f.energia.ec import ec
from pages.f.energia.ep import ep
from pages.f.energia.em import em
from pages.f.energia.tec import tec
from pages.f.energia.trabp import trabp
from pages.f.energia.wfnc import wfnc
from pages.f.energia.trabalho import trabalho
from pages.f.energia.ecalor import ecalor
from pages.f.energia.eint import eint
from pages.f.energia.ediss import ediss
from pages.f.energia.eutil import eutil
from pages.f.energia.pdiss import pdiss
from pages.f.energia.putil import putil
from pages.f.energia.pot import pot
from pages.f.energia.irradp import irradp
from pages.f.energia.irrade import irrade
from pages.f.energia.resist import resist
from pages.f.energia.resistividade import resistividade
from pages.f.energia.dpot import dpot
ener = ["Energia Cinética", "Energia Potencial", "Energia Mecânica", "Teorema da Energia Cinética", "Trabalho do Peso", "Trabalho das Forças Não Conservativas", "Trabalho", "Energia (calor)", "Energia Interna", "Energia dissipada", "Energia Útil", "Potência Dissipada", "Potência Útil", "Potência", "Irradiância (P)", "Irradiância (E)", "Resistência", "Resistividade", "Diferença de Potencial (gerador)"]
def ene():
    cal = ["Energia cinética (J)", "Massa (g)", "Velocidade (m/s)"]
    cols = st.beta_columns(2)
    q = cols[0].selectbox("Fórmula", ener)
    if q == "Energia Cinética":
        cal = ["Energia cinética (J)", "Massa (g)", "Velocidade (m/s)"]
        c = cols[1].selectbox("A Calcular", cal)
        ec(c)
    elif q == "Energia Potencial":
        cal = ["Energia potencial (J)", "Massa (g)", "Altura (m)"]
        c = cols[1].selectbox("A Calcular", cal)
        ep(c)
    elif q == "Energia Mecânica":
        cal = ["Energia mecânica (J)", "Energia cinética (J)", "Energia potencial (J)"]
        c = cols[1].selectbox("A Calcular", cal)
        em(c)
    elif q == "Teorema da Energia Cinética":
        cal = ["Trabalho (J)", "Energia cinética inicial (J)", "Energia cinética inicial (J)"]
        c = cols[1].selectbox("A Calcular", cal)
        tec(c)
    elif q == "Trabalho do Peso":
        cal = ["Trabalho do peso (J)", "Energia potencial final (J)", "Energia potencial inicial (J)"]
        c = cols[1].selectbox("A Calcular", cal)
        trabp(c)
    elif q == "Trabalho das Forças Não Conservativas":
        cal = ["Trabalho das forças não conservativas (J)", "Energia mecânica final (J)", "Energia mecânica inicial (J)"]
        c = cols[1].selectbox("A Calcular", cal)
        wfnc(c)
    elif q == "Trabalho":
        cal = ["Trabalho (J)","Força (N)", "Deslocamento (m)", "Ângulo α"]
        c = cols[1].selectbox("A Calcular", cal)
        trabalho(c)
    elif q == "Energia (calor)":
        cal = ["Energia (J)", "Massa (g)", "Capacidade Térmica Mássica (J/Kg/K)", "Variação da Temperatura (K)"]
        c = cols[1].selectbox("A Calcular", cal)
        ecalor(c)
        ####################
    elif q == "Energia Interna":
        cal = ["Energia interna (J)", "Calor (J)", "Trabalho (J)"]
        c = cols[1].selectbox("A Calcular", cal)
        eint(c)
    elif q == "Energia dissipada":
        cal = ["Energia Dissipada (J)", "Resistência (Ω)", "Corrente Elétrica (A)", "Variação do Tempo (s)"]
        c = cols[1].selectbox("A Calcular", cal)
        ediss(c)
    elif q == "Energia Útil":
        cal = ["Energia Útil (J)", "Diferença de Potencial (V)", "Corrente Elétrica (A)", "Variação do Tempo (s)"]
        c = cols[1].selectbox("A Calcular", cal)
        eutil(c)
    elif q == "Potência Dissipada":
        cal = ["Potência Dissipada (W)", "Resistência (Ω)", "Corrente Elétrica (A)"]
        c = cols[1].selectbox("A Calcular", cal)
        pdiss(c)
    elif q == "Potência Útil":
        cal = ["Potência Útil (W)", "Diferença de Potencial (V)", "Corrente Elétrica (A)"]
        c = cols[1].selectbox("A Calcular", cal)
        putil(c)
    elif q == "Potência":
        cal = ["Potência (W)", "Energia (J)", "Variação do Tempo (s)"]
        c = cols[1].selectbox("A Calcular", cal)
        pot(c)
    elif q == "Irradiância (P)":
        cal = ["Irradiância (W/m²)", "Potência (W)", "Área (m²)"]
        c = cols[1].selectbox("A Calcular", cal)
        irradp(c)
    elif q == "Irradiância (E)":
        cal = ["Irradiância (W/m²)", "Energia (J)", "Área (m²)", "Variação do Tempo (s)"]
        c = cols[1].selectbox("A Calcular", cal)
        irrade(c)
    elif q == "Resistência":
        cal = ["Resistência (Ω)", "Diferença de Potencial (V)", "Corrente Elétrica (A)"]
        c = cols[1].selectbox("A Calcular", cal)
        resist(c)
    elif q == "Resistividade":
        cal = ["Resistência (Ω)", "Resistividade (Ωm)", "Comprimento (m)", "Área (m²)"]
        c = cols[1].selectbox("A Calcular", cal)
        resistividade(c)
    elif q == "Diferença de Potencial (gerador)":
        cal = ["Diferença de Potencial (V)", "Força Eletromotriz (V)", "Resistência Interna (Ω)", "Corrente Elétrica (A)"]
        c = cols[1].selectbox("A Calcular", cal)
        dpot(c)