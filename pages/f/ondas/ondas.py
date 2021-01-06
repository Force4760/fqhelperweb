import streamlit as st
from pages.f.ondas.conda import l
from pages.f.ondas.fei import fei
from pages.f.ondas.iref import n
from pages.f.ondas.freq import freq
from pages.f.ondas.fmag import fmag
from pages.f.ondas.snell import snell
quant = ["Comprimento de onda", "Força eletromotriz induzida", "Fluxo magnético", "Índice de refração", "Lei de Snell", "Frequência"]
def o():
    cal = ["Comprimento de onda (m)", "Velocidade (m/s)", "Frequência (Hz)"]
    cols = st.beta_columns(2)
    q = cols[0].selectbox("Fórmula", quant)
    if q == "Comprimento de onda":
        cal = ["Comprimento de onda (m)", "Velocidade (m/s)", "Frequência (Hz)"]
        c = cols[1].selectbox("A Calcular", cal)
        l(c)
    elif q == "Força eletromotriz induzida":
        cal = ["Força eletromotriz induzida (V)", "Variação do fluxo magnético (Wb)", "Variação do tempo (s)"]
        c = cols[1].selectbox("A Calcular", cal)
        fei(c)
    elif q == "Índice de refração":
        cal = ["Índice de refração", "Velocidade (m/s)"]
        c = cols[1].selectbox("A Calcular", cal)
        n(c)
    elif q == "Frequência":
        cal = ["Frequência (Hz)", "Período (s)"]
        c = cols[1].selectbox("A Calcular", cal)
        freq(c)
    elif q == "Fluxo magnético":
        cal = ["Fluxo magnético (Wb)", "Campo magnético (T)", "Área (m²)", "Ângulo α"]
        c = cols[1].selectbox("A Calcular", cal)
        fmag(c)
    elif q == "Lei de Snell":
        cal = ["Índice de refração 1", "Ângulo α1", "Índice de refração 2", "Ângulo α2"]
        c = cols[1].selectbox("A Calcular", cal)
        snell(c)