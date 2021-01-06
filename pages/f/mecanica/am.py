import streamlit as st
import math
def calcA(v, t):
    a = v / t
    return f"a = {a} m/s²"
      

def calcV(a, t):
    v = t * a
    return f'Δv = {v} m/s'

def calcT(a, v):
    t = v / a
    return f"Δt = {t} s"

def calc(a, v, t):
    try:
        if (a == "" and v != "" and t != ""):
            result = calcA(v, t)
        elif (v == "" and a != "" and t != ""):
            result = calcV(a, t)
        elif (t == "" and v != "" and a != ""):
            result = calcT(a, v)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def am(b):
    result = 'a = 0 m/s²'
    st.latex(r"a = \frac{\Delta v}{\Delta t}")
    if b == "Aceleração Centrípeta (m/s²)":
        result = 'ac = 0 m/s²'
        a = ""
        v = st.number_input("Δ Velocidade (m/s)", format="%g" , step=1.0)
        t = st.number_input("Δ Tempo (s)", format="%g" , step=1.0)
    elif b == "Δ Velocidade (m/s)":
        result = "Δv = 0 m/s"
        a = st.number_input("Aceleração Centrípeta (m/s²)", format="%g" , step=1.0)
        v = ""
        t = st.number_input("Δ Tempo (s)", format="%g" , step=1.0)
    elif b == "Δ Tempo (s)":
        result = "Δt = 0 s"
        a = st.number_input("Aceleração Centrípeta (m/s²)", format="%g" , step=1.0)
        v = st.number_input("Δ Velocidade (m/s)", format="%g" , step=1.0)
        t = ""
    if st.button("Calcular"):
         result = calc(a,v,t)
    st.title(result)