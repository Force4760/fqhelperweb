import streamlit as st
import math
def calcE(u, i, t):
    e = u * i * t
    return f"E = {e} J"

def calcU(e, i, t):
    u = e / (i * t)
    return f"U = {u} V"

def calcI(e, u, t):
    i = e / (u * t)
    return f"I = {i} A"

def calcT(e, u, i):
    t = e / (u * i)
    return f"Δt = {t} s"


def calc(e, r, i, t):
    try:
        if (e == "" and r != "" and i != "" and t != ""):
            result = calcE(r, i, t)
        elif (e != "" and r == "" and i != "" and t != ""):
            result = calcU(e, i, t)
        elif (e != "" and r != "" and i == "" and t != ""):
            result = calcI(e, r, t)
        elif (e != "" and r != "" and i != "" and t == ""):
            result = calcT(e, r, i)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def eutil(b):
    result = 'E = 0 J'
    st.latex(r"E = U I \Delta t")
    if b == "Energia Dissipada (J)":
        result = 'E = 0 J'
        e = ""
        u = st.number_input("Diferença de Potencial (V)", format="%g" , step=1.0)
        i = st.number_input("Corrente Elétrica (A)", format="%g" , step=1.0)
        t = st.number_input( "Δ Tempo (s)", format="%g" , step=1.0)
    elif b == "Diferença de Potencial (V)":
        result = "R = 0 Ω"
        e = st.number_input("Energia Dissipada (J)", format="%g" , step=1.0)
        u = ""
        i = st.number_input("Corrente Elétrica (A)", format="%g" , step=1.0)
        t = st.number_input( "Δ Tempo (s)", format="%g" , step=1.0)
    elif b == "Corrente Elétrica (A)":
        result = "I = 0 A"
        e = st.number_input("Energia Dissipada (J)", format="%g" , step=1.0)
        u = st.number_input("Diferença de Potencial (V)", format="%g" , step=1.0)
        i = ""
        t = st.number_input("Δ Tempo (s)", format="%g" , step=1.0)
    elif b == "Δ Tempo (s)":
        result = f'Δt = 0 s'
        e = st.number_input("Energia Dissipada (J)", format="%g" , step=1.0)
        u = st.number_input("Diferença de Potencial (V)", format="%g" , step=1.0)
        i = st.number_input("Corrente Elétrica (A)", format="%g" , step=1.0)
        t = ""
    if st.button("Calcular"):
         result = calc(e, u, i, t)
    st.title(result)