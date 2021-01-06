import streamlit as st
import math
def calcEr(p, a):
    e = p / a
    return f"Er = {e} W/m²"

def calcP(e, a):
    p = e * a
    return f"P = {p} W"

def calcA(e, p):
    a = p / e
    return f"A = {a} m²"



def calc(e, p, a):
    try:
        if (e == "" and p != "" and a != ""):
            result = calcEr(p, a)
        elif (e != "" and p == "" and a != ""):
            result = calcP(e, a)
        elif (e != "" and p != "" and a == ""):
            result = calcA(e, p)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def irradp(b):
    result = 'Er = 0 W/m²'
    st.latex(r"Er = \frac{P}{A}")
    if b == "Irradiância (W/m²)":
        result = 'Er = 0 W/m²'
        e = ""
        p = st.number_input("Potência (W)", format="%g" , step=1.0)
        a = st.number_input("Área (m²)", format="%g" , step=1.0)
    elif b == "Potência (W)":
        result = "P = 0 W"
        e = st.number_input("Irradiância (W/m²)", format="%g" , step=1.0)
        p = ""
        a = st.number_input("Área (m²)", format="%g" , step=1.0)
    elif b == "Área (m²)":
        result = "A = 0 m²"
        e = st.number_input("Irradiância (W/m²)", format="%g" , step=1.0)
        p = st.number_input("Potência (W)", format="%g" , step=1.0)
        a = ""
    if st.button("Calcular"):
         result = calc(e, p, a)
    st.title(result)