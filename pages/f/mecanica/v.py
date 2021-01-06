import streamlit as st
import math
def calcV(w, r):
    v = w * r
    return f"v = {v} m/s"
      

def calcW(v, r):
    w = v / r
    return f'ω  = {w} rad/s'

def calcR(v, w):
    r = v / w
    return f"R = {r} m"

def calc(v, w, r):
    try:
        if (v == "" and w != "" and r != ""):
            result = calcV(w, r)
        elif (w == "" and v != "" and r != ""):
            result = calcW(v, r)
        elif (r == "" and w != "" and v != ""):
            result = calcR(v, w)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def v(b):
    result = 'v = 0 m/s'
    st.latex(r"v = \omega R")
    if b == "Velocidade (m/s)":
        result = 'v = 0 m/s'
        v = ""
        w = st.number_input("Velocidade Angular (rad/s)", format="%g" , step=1.0)
        r = st.number_input("Raio (m)", format="%g" , step=1.0)
    elif b == "Velocidade Angular (rad/s)":
        result = "ω = 0 rad/s"
        v = st.number_input("Velocidade (m/s)", format="%g" , step=1.0)
        w = ""
        r = st.number_input("Raio (m)", format="%g" , step=1.0)
    elif b == "Raio (m)":
        result = "R = 0 m"
        v = st.number_input("Velocidade (m/s)", format="%g" , step=1.0)
        w = st.number_input("Velocidade Angular (rad/s)", format="%g" , step=1.0)
        r = ""
    if st.button("Calcular"):
         result = calc(v, w,r)
    st.title(result)