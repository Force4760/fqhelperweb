import streamlit as st
import math
def calcR(u, i):
    r = u / i
    return f"R = {r} Ω"

def calcU(r, i):
    u = r * i
    return f"U = {u} V"

def calcI(r, u):
    i = u / r
    return f"I = {i} A"



def calc(r, u, i):
    try:
        if (r == "" and u != "" and i != ""):
            result = calcR(u, i)
        elif (r != "" and u == "" and i != ""):
            result = calcU(r, i)
        elif (r != "" and u != "" and i == ""):
            result = calcI(r, u)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def resist(b):
    result = 'R = 0 Ω'
    st.latex(r"R = \frac{U}{I}")
    if b == "Resistência (Ω)":
        result = 'R = 0 Ω'
        r = ""
        u = st.number_input("Diferença de Potencial (V)", format="%g" , step=1.0)
        i = st.number_input("Corrente Elétrica (A)", format="%g" , step=1.0)
    elif b == "Diferença de Potencial (V)":
        result = "U = 0 V"
        r = st.number_input("Resistência (Ω)", format="%g" , step=1.0)
        u = ""
        i = st.number_input("Corrente Elétrica (A)", format="%g" , step=1.0)
    elif b == "Corrente Elétrica (A)":
        result = "I = 0 A"
        r = st.number_input("Resistência (Ω)", format="%g" , step=1.0)
        u = st.number_input("Diferença de Potencial (V)", format="%g" , step=1.0)
        i = ""
    if st.button("Calcular"):
         result = calc(r, u, i)
    st.title(result)