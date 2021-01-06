import math
import streamlit as st
def calcE(m, v):
    e = (m * (v * v)) / 2
    return f"Ec = {e} J"
      

def calcM(e, v):
    m = (e / (v * v)) * 2
    return f'm = {m} g'

def calcV(e, m):
    v = math.sqrt((e / m) * 2)
    return f"v = {v} m/s"

def calc(e, m, v):
    try:
        if (e == "" and m != "" and v != ""):
            result = calcE(m, v)
        elif (m == "" and v != "" and e != ""):
            result = calcM(e, v)
        elif (v == "" and m != "" and e != ""):
            result = calcV(e, m)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def ec(t):
    result = 'Ec = 0 J'
    st.latex(r"E_c = \frac{1}{2} m v^2")
    if t == "Energia cinética (J)":
        result = 'Ec = 0 J'
        e = ""
        m = st.number_input("Massa (g)", format="%g" , step=1.0)
        v = st.number_input("Velocidade (m/s)", format="%g" , step=1.0)
    elif t == "Massa (g)":
        result = "m = 0 g"
        m = ""
        e = st.number_input("Energia cinética (J)", format="%g" , step=1.0)
        v = st.number_input("Velocidade (m/s)", format="%g" , step=1.0)
    elif t == "Velocidade (m/s)":
        result = "v = 0 m/s"
        v = ""
        e = st.number_input("Energia cinética (J)", format="%g" , step=1.0)
        m = st.number_input("Massa (g)", format="%g" , step=1.0)
    if st.button("Calcular"):
         result = calc(e, m, v)
    st.title(result)