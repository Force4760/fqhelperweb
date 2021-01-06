import streamlit as st
import math
def calcA(v, r):
    a = v * v / r
    return f"ac = {a} m/s²"
      

def calcV(a, r):
    v = math.sqrt(a * r)
    return f'v = {v} m/s'

def calcR(a, v):
    r = v * v / a
    return f"R = {r} m"

def calc(a, v, r):
    try:
        if (a == "" and v != "" and r != ""):
            result = calcA(v, r)
        elif (v == "" and a != "" and r != ""):
            result = calcV(a, r)
        elif (r == "" and v != "" and a != ""):
            result = calcR(a, v)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def ac1(t):
    result = 'ac = 0 m/s²'
    st.latex(r"a_c = \frac{v^2}{R}")
    if t == "Aceleração Centrípeta (m/s²)":
        result = 'ac = 0 m/s²'
        a = ""
        v = st.number_input("Velocidade (m/s)", format="%g" , step=1.0)
        r = st.number_input("Raio (m)", format="%g" , step=1.0)
    elif t == "Velocidade (m/s)":
        result = "v = 0 m/s"
        a = st.number_input("Aceleração Centrípeta (m/s²)", format="%g" , step=1.0)
        v = ""
        r = st.number_input("Raio (m)", format="%g" , step=1.0)
    elif t == "Raio (m)":
        result = "R = 0 m"
        a = st.number_input("Aceleração Centrípeta (m/s²)", format="%g" , step=1.0)
        v = st.number_input("Velocidade (m/s)", format="%g" , step=1.0)
        r = ""
    if st.button("Calcular"):
         result = calc(a,v,r)
    st.title(result)