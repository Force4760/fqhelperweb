import streamlit as st
import math
def calcW(t):
    w = 2 * math.pi / t
    return f"ω = {w} rad/s"
      

def calcT(w):
    t = 2 * math.pi / w
    return f'T = {t} s'

def calc(w, t):
    try:
        if (w == "" and t != ""):
            result = calcW(t)
        elif (t == "" and w != ""):
            result = calcT(w)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def vang1(b):
    result = 'ω = 0 rad/s'
    st.latex(r"\omega = \frac{2 \pi}{T}")
    if b == "Velocidade Angular (rad/s)":
        result = 'ω = 0 rad/s'
        w = ""
        t = st.number_input("Período (s)", format="%g" , step=1.0)
    elif b == "Período (s)":
        result = "T = 0 s"
        w = st.number_input("Velocidade Angular (rad/s)", format="%g" , step=1.0)
        t = ""
    if st.button("Calcular"):
         result = calc(w, t)
    st.title(result)