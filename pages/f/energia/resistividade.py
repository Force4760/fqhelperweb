import streamlit as st
import math
def calcR(p, l, a):
    r = p * l / a
    return f"R = {r} Ω"

def calcP(r, l, a):
    p = r * a / l
    return f"ρ = {p} Ωm"

def calcL(r, p, a):
    l = r * a / p
    return f"l = {l} m"

def calcA(r, p, l):
    a = l / ( r / p )
    return f"A = {a} m²"



def calc(r, p, l, a):
    try:
        if (r == "" and p != "" and l != "" and a != ""):
            result = calcR(p, l, a)
        elif (r != "" and p == "" and l != "" and a != ""):
            result = calcP(r, l, a)
        elif (r != "" and p != "" and l == "" and a != ""):
            result = calcL(r, p, a)
        elif (r != "" and p != "" and l != "" and a == ""):
            result = calcA(r, p, l)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def resistividade(b):
    result = 'R = 0 Ω'
    st.latex(r"R = \rho\frac{l}{A}")
    if b == "Resistência (Ω)":
        result = 'R = 0 Ω'
        r = ""
        p = st.number_input("Resistividade (Ωm)", format="%g" , step=1.0)
        l = st.number_input("Comprimento (m)", format="%g" , step=1.0)
        a = st.number_input("Área (m²)", format="%g" , step=1.0)
    elif b == "Resistividade (Ωm)":
        result = "ρ = 0 Ωm"
        r = st.number_input("Resistência (Ω)", format="%g" , step=1.0)
        p = ""
        l = st.number_input("Comprimento (m)", format="%g" , step=1.0)
        a = st.number_input("Área (m²)", format="%g" , step=1.0)
    elif b == "Comprimento (m)":
        result = "l = 0 m"
        r = st.number_input("Resistência (Ω)", format="%g" , step=1.0)
        p = st.number_input("Resistividade (Ωm)", format="%g" , step=1.0)
        l = ""
        a = st.number_input("Área (m²)", format="%g" , step=1.0)
    elif b == "Área (m²)":
        result = "A = 0 m²"
        r = st.number_input("Resistência (Ω)", format="%g" , step=1.0)
        p = st.number_input("Resistividade (Ωm)", format="%g" , step=1.0)
        l = st.number_input("Comprimento (m)", format="%g" , step=1.0)
        a = ""
    if st.button("Calcular"):
         result = calc(r, p, l, a)
    st.title(result)