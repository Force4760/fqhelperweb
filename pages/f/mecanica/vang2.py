import streamlit as st
import math
def calcW(f):
    w = 2 * math.pi * f
    return f"ω = {w} rad/s"
      

def calcF(w):
    f = w / (2 * math.pi)
    return f'f = {f} Hz'

def calc(w, f):
    try:
        if (w == "" and f != ""):
            result = calcW(f)
        elif (f == "" and w != ""):
            result = calcF(w)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def vang2(b):
    result = 'ω = 0 rad/s'
    st.latex(r"\omega = 2 \pi f")
    if b == "Velocidade Angular (rad/s)":
        result = 'ω = 0 rad/s'
        w = ""
        f = st.number_input("Frequência (Hz)", format="%g" , step=1.0)
    elif b == "Frequência (Hz)":
        result = "f = 0 Hz"
        w = st.number_input("Velocidade Angular (rad/s)", format="%g" , step=1.0)
        f = ""
    if st.button("Calcular"):
         result = calc(w, f)
    st.title(result)