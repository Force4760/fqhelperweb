import streamlit as st
import math
def calcU(e, r, i):
    u = e - (r * i)
    return f"U = {u} V"

def calcE(u, r, i):
    e = u + (r * i)
    return f"ε = {e} V"

def calcR(u, e, i):
    r = ( - u + e ) / i
    return f"r = {r} Ω"

def calcI(u, e, r):
    i = ( - u + e ) / r
    return f"I = {i} A"



def calc(u, e, r, i):
    try:
        if (u == "" and e != "" and r != "" and i != ""):
            result = calcU(e, r, i)
        elif (u != "" and e == "" and r != "" and i != ""):
            result = calcE(u, r, i)
        elif (u != "" and e != "" and r == "" and i != ""):
            result = calcR(u, e, i)
        elif (u != "" and e != "" and r != "" and i == ""):
            result = calcI(u, e, r)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def dpot(b):
    result = 'U = 0 V'
    st.latex(r"U = \varepsilon - r I")
    if b == "Diferença de Potencial (V)":
        result = 'U = 0 V'
        u = ""
        e = st.number_input("Força Eletromotriz (V)", format="%g" , step=1.0)
        r = st.number_input("Resistência Interna (Ω)", format="%g" , step=1.0)
        i = st.number_input("Corrente Elétrica (A)", format="%g" , step=1.0)
    elif b == "Força Eletromotriz (V)":
        result = "ε = 0 V"
        u = st.number_input("Diferença de Potencial (V)", format="%g" , step=1.0)
        e = ""
        r = st.number_input("Resistência Interna (Ω)", format="%g" , step=1.0)
        i = st.number_input("Corrente Elétrica (A)", format="%g" , step=1.0)
    elif b == "Resistência Interna (Ω)":
        result = "r = 0 Ω"
        u = st.number_input("Diferença de Potencial (V)", format="%g" , step=1.0)
        e = st.number_input("Força Eletromotriz (V)", format="%g" , step=1.0)
        r = ""
        i = st.number_input("Corrente Elétrica (A)", format="%g" , step=1.0)
    elif b == "Corrente Elétrica (A)":
        result = "I = 0 A"
        u = st.number_input("Diferença de Potencial (V)", format="%g" , step=1.0)
        e = st.number_input("Força Eletromotriz (V)", format="%g" , step=1.0)
        r = st.number_input("Resistência Interna (Ω)", format="%g" , step=1.0)
        i = ""
    if st.button("Calcular"):
         result = calc(u, e, r, i)
    st.title(result)