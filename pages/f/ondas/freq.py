import streamlit as st

def calcf(t):
    f= 1 / t
    return f"f = {f} Hz"

def calct(f):
    t = 1 / f
    return f"T = {t} s"


def calc(f,t):
    try:
        if (f== "" and t!= ""):
            result = calcf(t)
        elif (t== "" and f!= ""):
            result = calct(f)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def freq(c):
    result = 'f = 0 Hz'
    st.latex(r"f = \frac{1}{T}")
    if c == "Frequência (Hz)":
        result = 'f = 0 Hz'
        f= ""
        t= st.number_input("Período (s)", format="%g" , step=1.0)
    elif c == "Período (s)":
        result = "T = 0 s"
        t= ""
        f= st.number_input("Frequência (Hz)", format="%g" , step=1.0)
    if st.button("Calcular"):
         result = calc(f, t)
    st.title(result)