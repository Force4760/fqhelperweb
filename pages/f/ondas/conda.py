import streamlit as st

def calcl(v, f):
    l = v / f
    return f"λ = {l} m"

def calcv(l, f):
    v = l * f
    return f"v = {v} m/s"

def calf(l, v):
    f = v / l
    return f"f = {f} Hz"

def calc(l,v,f):
    try:
        if (l == "" and v != "" and f != ""):
            result = calcl(v, f)
        elif (v == "" and f != "" and l != ""):
            result = calcv(l, f)
        elif (f == "" and v != "" and l != ""):
            result = calf(l, v)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def l(t):
    result = 'λ = 0 m'
    st.latex(r"\lambda = \frac{v}{f}")
    if t == "Comprimento de onda (m)":
        result = 'λ = 0 m'
        l = ""
        v = st.number_input("Velocidade (m/s)", format="%g" , step=1.0)
        f = st.number_input("Frequência (Hz)", format="%g" , step=1.0)
    elif t == "Velocidade (m/s)":
        result = "v = 0 m/s"
        v = ""
        l = st.number_input("Comprimento de onda (m)", format="%g" , step=1.0)
        f = st.number_input("Frequência (Hz)", format="%g" , step=1.0)
    elif t == "Frequência (Hz)":
        result = "f = 0 Hz"
        f = ""
        l = st.number_input("Comprimento de onda (m)", format="%g" , step=1.0)
        v = st.number_input("Velocidade (m/s)", format="%g" , step=1.0)
    if st.button("Calcular"):
         result = calc(l, v, f)
    st.title(result)