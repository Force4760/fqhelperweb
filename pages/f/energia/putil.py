import streamlit as st
import math
def calcP(r, i):
    p = r * i
    return f"P = {p} W"

def calcU(e, i):
    r = e / i
    return f"U = {r} V"

def calcI(e, r):
    i = e / r
    return f"I = {i} A"



def calc(e, r, i):
    try:
        if (e == "" and r != "" and i != ""):
            result = calcP(r, i)
        elif (e != "" and r == "" and i != ""):
            result = calcU(e, i)
        elif (e != "" and r != "" and i == ""):
            result = calcI(e, r)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def putil(b):
    result = 'P = 0 W'
    st.latex(r"P = U I")
    if b == "Potência Útil (W)":
        result = 'P = 0 W'
        e = ""
        r = st.number_input("Diferença de Potencial (V)", format="%g" , step=1.0)
        i = st.number_input("Corrente Elétrica (A)", format="%g" , step=1.0)
    elif b == "Diferença de Potencial (V)":
        result = "U = 0 V"
        e = st.number_input("Potência Útil (W)", format="%g" , step=1.0)
        r = ""
        i = st.number_input("Corrente Elétrica (A)", format="%g" , step=1.0)
    elif b == "Corrente Elétrica (A)":
        result = "I = 0 A"
        e = st.number_input("Potência Útil (W)", format="%g" , step=1.0)
        r = st.number_input("Diferença de Potencial (V)", format="%g" , step=1.0)
        i = ""
    if st.button("Calcular"):
         result = calc(e, r, i)
    st.title(result)