import streamlit as st

def calce(f, t):
    e = f / t
    return f"|Ɛ| = {e} V"

def calcf(e, t):
    f = e * t
    return f"|Δϕ| = {f} Wb"

def calct(e, f):
    t = f / e
    return f"|Δt| = {t} s"

def calc(e,f,t):
    try:
        if (e == "" and f != "" and t != ""):
            result = calce(f, t)
        elif (f == "" and e != "" and t != ""):
            result = calcf(e, t)
        elif (t == "" and e != "" and f != ""):
            result = calct(e, f)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def fei(t):
    result = '|Ɛ| = 0 V'
    st.latex(r"|\varepsilon_i| = \frac{|\Delta\Phi|}{|\Delta t|}")
    if t == "Força eletromotriz induzida (V)":
        result = '|Ɛ| = 0 V'
        e = ""
        f = st.number_input("Variação do fluxo magnético (Wb)", format="%g" , step=1.0)
        t = st.number_input("Variação do tempo (s)", format="%g" , step=1.0)
    elif t == "Variação do fluxo magnético (Wb)":
        result = "|Δϕ| = 0 Wb"
        f = ""
        e = st.number_input("Força eletromotriz induzida (V)", format="%g" , step=1.0)
        t = st.number_input("Variação do tempo (s)", format="%g" , step=1.0)
    elif t == "Variação do tempo (s)":
        result = "|Δt| = 0 s"
        t = ""
        e = st.number_input("Força eletromotriz induzida (V)", format="%g" , step=1.0)
        f = st.number_input("Variação do fluxo magnético (Wb)", format="%g" , step=1.0)
    if st.button("Calcular"):
         result = calc(e, f, t)
    st.title(result)