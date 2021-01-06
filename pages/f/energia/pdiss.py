import streamlit as st
import math
def calcP(r, i):
    p = r * i * i
    return f"P = {p} W"

def calcR(e, i):
    r = e / (i * i)
    return f"R = {r} Ω"

def calcI(e, r):
    i = math.sqrt((e / r))
    return f"I = {i} A"



def calc(e, r, i):
    try:
        if (e == "" and r != "" and i != ""):
            result = calcP(r, i)
        elif (e != "" and r == "" and i != ""):
            result = calcR(e, i)
        elif (e != "" and r != "" and i == ""):
            result = calcI(e, r)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def pdiss(b):
    result = 'P = 0 W'
    st.latex(r"P = R I^2")
    if b == "Potência Dissipada (W)":
        result = 'P = 0 W'
        e = ""
        r = st.number_input("Resistência (Ω)", format="%g" , step=1.0)
        i = st.number_input("Corrente Elétrica (A)", format="%g" , step=1.0)
    elif b == "Resistência (Ω)":
        result = "R = 0 Ω"
        e = st.number_input("Potência Dissipada (W)", format="%g" , step=1.0)
        r = ""
        i = st.number_input("Corrente Elétrica (A)", format="%g" , step=1.0)
    elif b == "Corrente Elétrica (A)":
        result = "I = 0 A"
        e = st.number_input("Potência Dissipada (W)", format="%g" , step=1.0)
        r = st.number_input("Resistência (Ω)", format="%g" , step=1.0)
        i = ""
    if st.button("Calcular"):
         result = calc(e, r, i)
    st.title(result)