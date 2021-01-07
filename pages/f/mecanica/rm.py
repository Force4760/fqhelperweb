import streamlit as st
import math
def calcR(s, t):
    r = s / t
    return f"rm = {r} m/s"
      

def calcS(r, t):
    s = r * t
    return f'Δs = {s} m'

def calcT(r, s):
    t = s / r
    return f"Δt = {t} s"

def calc(r, s, t):
    try:
        if (r == "" and s != "" and t != ""):
            result = calcR(s, t)
        elif (s == "" and r != "" and t != ""):
            result = calcS(r, t)
        elif (t == "" and s != "" and r != ""):
            result = calcT(r, s)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def rm(b):
    result = 'rm = 0 m/s'
    st.latex(r"r_m = \frac{\Delta s}{\Delta t}")
    if b == "Rapidez Média (m/s)":
        result = 'rm = 0 m/s'
        r = ""
        s = st.number_input("Distância Percorrida (m)", format="%g" , step=1.0)
        t = st.number_input("Variação do Tempo (s)", format="%g" , step=1.0)
    elif b == "Distância Percorrida (m)":
        result = "Δs = 0 m"
        r = st.number_input("Rapidez Média (m/s)", format="%g" , step=1.0)
        s = ""
        t = st.number_input("Variação do Tempo (s)", format="%g" , step=1.0)
    elif b == "Variação do Tempo (s)":
        result = "Δt = 0 s"
        r = st.number_input("Rapidez Média (m/s)", format="%g" , step=1.0)
        s = st.number_input("Distância Percorrida (m)", format="%g" , step=1.0)
        t = ""
    if st.button("Calcular"):
         result = calc(r,s,t)
    st.title(result)