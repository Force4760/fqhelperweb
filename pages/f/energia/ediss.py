import streamlit as st
import math
def calcE(r, i, t):
    e = r * i * i * t
    return f"E = {e} J"

def calcR(e, i, t):
    r = e / (i * i * t)
    return f"R = {r} Ω"

def calcI(e, r, t):
    i = math.sqrt((e / (r * t)))
    return f"I = {i} A"

def calcT(e, r, i):
    t = e / (i * i * r)
    return f"Δt = {t} s"


def calc(e, r, i, t):
    try:
        if (e == "" and r != "" and i != "" and t != ""):
            result = calcE(r, i, t)
        elif (e != "" and r == "" and i != "" and t != ""):
            result = calcR(e, i, t)
        elif (e != "" and r != "" and i == "" and t != ""):
            result = calcI(e, r, t)
        elif (e != "" and r != "" and i != "" and t == ""):
            result = calcT(e, r, i)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def ediss(b):
    result = 'E = 0 J'
    st.latex(r"E = R I^2 \Delta t")
    if b == "Energia Dissipada (J)":
        result = 'E = 0 J'
        e = ""
        r = st.number_input("Resistência (Ω)", format="%g" , step=1.0)
        i = st.number_input("Corrente Elétrica (A)", format="%g" , step=1.0)
        t = st.number_input( "Variação do Tempo (s)", format="%g" , step=1.0)
    elif b == "Resistência (Ω)":
        result = "R = 0 Ω"
        e = st.number_input("Energia Dissipada (J)", format="%g" , step=1.0)
        r = ""
        i = st.number_input("Corrente Elétrica (A)", format="%g" , step=1.0)
        t = st.number_input( "Variação do Tempo (s)", format="%g" , step=1.0)
    elif b == "Corrente Elétrica (A)":
        result = "I = 0 A"
        e = st.number_input("Energia Dissipada (J)", format="%g" , step=1.0)
        r = st.number_input("Resistência (Ω)", format="%g" , step=1.0)
        i = ""
        t = st.number_input("Variação do Tempo (s)", format="%g" , step=1.0)
    elif b == "Variação do Tempo (s)":
        result = f'Δt = 0 s'
        e = st.number_input("Energia Dissipada (J)", format="%g" , step=1.0)
        r = st.number_input("Resistência (Ω)", format="%g" , step=1.0)
        i = st.number_input("Corrente Elétrica (A)", format="%g" , step=1.0)
        t = ""
    if st.button("Calcular"):
         result = calc(e, r, i, t)
    st.title(result)