import streamlit as st
import math
def calcE(m, c, t):
    e = m * c * t
    return f"E = {e} J"

def calcM(e, c, t):
    m = e / (c * t)
    return f"m = {m} g"

def calcC(e, m, t):
    c = e / (m * t)
    return f"c = {c} J/Kg/K"

def calcT(e, m, c):
    t = e / (m * c)
    return f"ΔT = {t} K"


def calc(e, m, c, t):
    try:
        if (e == "" and m != "" and c != "" and t != ""):
            result = calcE(m, c, t)
        elif (e != "" and m == "" and c != "" and t != ""):
            result = calcM(e, c, t)
        elif (e != "" and m != "" and c == "" and t != ""):
            result = calcC(e, m, t)
        elif (e != "" and m != "" and c != "" and t == ""):
            result = calcT(e, m, c)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def ecalor(b):
    result = 'E = 0 J'
    st.latex(r"E = m c \Delta T")
    if b == "Energia (J)":
        result = 'E = 0 J'
        e = ""
        m = st.number_input("Massa (g)", format="%g" , step=1.0)
        c = st.number_input("Capacidade Térmica Mássica (J/Kg/K)", format="%g" , step=1.0)
        t = st.number_input( "Variação da Temperatura (K)", format="%g" , step=1.0)
    elif b == "Massa (g)":
        result = "m = 0 g"
        e = st.number_input("Energia (J)", format="%g" , step=1.0)
        m = ""
        c = st.number_input("Capacidade Térmica Mássica (J/Kg/K)", format="%g" , step=1.0)
        t = st.number_input( "Variação da Temperatura (K)", format="%g" , step=1.0)
    elif b == "Capacidade Térmica Mássica (J/Kg/K)":
        result = "c = 0 J/Kg/K"
        e = st.number_input("Energia (J)", format="%g" , step=1.0)
        m = st.number_input("Massa (g)", format="%g" , step=1.0)
        c = ""
        t = st.number_input("Variação da Temperatura (K)", format="%g" , step=1.0)
    elif b == "Variação da Temperatura (K)":
        result = f'ΔT = 0 K'
        e = st.number_input("Energia (J)", format="%g" , step=1.0)
        m = st.number_input("Massa (g)", format="%g" , step=1.0)
        c = st.number_input("Capacidade Térmica Mássica (J/Kg/K)", format="%g" , step=1.0)
        t = ""
    if st.button("Calcular"):
         result = calc(e, m, c, t)
    st.title(result)