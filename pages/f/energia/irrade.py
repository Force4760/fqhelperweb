import streamlit as st
import math
def calcEr(p, a, t):
    e = p / (a * t)
    return f"Er = {e} W/m²"

def calcP(e, a, t):
    p = e * a * t
    return f"E = {e} J"

def calcA(e, p, t):
    a = p / (e * t)
    return f"A = {a} m²"

def calcT(e, p, a):
    t = p / (e * a)
    return f"Δt = {t} s"



def calc(e, p, a, t):
    try:
        if (e == "" and p != "" and a != "" and t != ""):
            result = calcEr(p, a, t)
        elif (e != "" and p == "" and a != "" and t != ""):
            result = calcP(e, a, t)
        elif (e != "" and p != "" and a == "" and t != ""):
            result = calcA(e, p, t)
        elif (e != "" and p != "" and a != "" and t == ""):
            result = calcT(e, p, a)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def irrade(b):
    result = 'Er = 0 W/m²'
    st.latex(r"Er = \frac{E}{A \Delta t}")
    if b == "Irradiância (W/m²)":
        result = 'Er = 0 W/m²'
        e = ""
        p = st.number_input("Energia (J)", format="%g" , step=1.0)
        a = st.number_input("Área (m²)", format="%g" , step=1.0)
        t = st.number_input("Δ Tempo (s)", format="%g" , step=1.0)
    elif b == "Energia (J)":
        result = "E = 0 J"
        e = st.number_input("Irradiância (W/m²)", format="%g" , step=1.0)
        p = ""
        a = st.number_input("Área (m²)", format="%g" , step=1.0)
        t = st.number_input("Δ Tempo (s)", format="%g" , step=1.0)
    elif b == "Área (m²)":
        result = "A = 0 m²"
        e = st.number_input("Irradiância (W/m²)", format="%g" , step=1.0)
        p = st.number_input("Energia (J)", format="%g" , step=1.0)
        a = ""
        t = st.number_input("Δ Tempo (s)", format="%g" , step=1.0)
    elif b == "Δ Tempo (s)":
        result = "Δt = 0 s"
        e = st.number_input("Irradiância (W/m²)", format="%g" , step=1.0)
        p = st.number_input("Energia (J)", format="%g" , step=1.0)
        a = st.number_input("Área (m²)", format="%g" , step=1.0)
        t = ""
    if st.button("Calcular"):
         result = calc(e, p, a, t)
    st.title(result)