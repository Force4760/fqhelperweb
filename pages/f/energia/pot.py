import streamlit as st
import math
def calcP(e, t):
    p = e / t
    return f"P = {p} W"

def calcE(p, t):
    e = p * t
    return f"E = {e} J"

def calcT(p, e):
    t = e / p
    return f"Δt = {t} s"



def calc(p, e, t):
    try:
        if (p == "" and e != "" and t != ""):
            result = calcP(e, t)
        elif (p != "" and e == "" and t != ""):
            result = calcE(p, t)
        elif (p != "" and e != "" and t == ""):
            result = calcT(p, e)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def pot(b):
    result = 'P = 0 W'
    st.latex(r"P = \frac{E}{\Delta t}")
    if b == "Potência (W)":
        result = 'P = 0 W'
        p = ""
        e = st.number_input("Energia (J)", format="%g" , step=1.0)
        t = st.number_input("Δ Tempo (s)", format="%g" , step=1.0)
    elif b == "Energia (J)":
        result = "E = 0 J"
        p = st.number_input("Potência (W)", format="%g" , step=1.0)
        e = ""
        t = st.number_input("Δ Tempo (s)", format="%g" , step=1.0)
    elif b == "Δ Tempo (s)":
        result = "Δt = 0 s"
        p = st.number_input("Potência (W)", format="%g" , step=1.0)
        e = st.number_input("Energia (J)", format="%g" , step=1.0)
        t = ""
    if st.button("Calcular"):
         result = calc(p, e, t)
    st.title(result)