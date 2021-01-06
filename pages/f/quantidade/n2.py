import streamlit as st

def calcn(m, mm):
    n = m / mm
    return f"n = {n} mol"

def calcm(n, mm):
    m = mm * n
    return f"m = {m} g"

def calcmm(n, m):
    mm = m / n
    return f"M = {mm} g/mol"

def calc(n,m,mm):
    try:
        if (n == "" and m != "" and mm != ""):
            result = calcn(m, mm)
        elif (m == "" and mm != "" and n != ""):
            result = calcm(n,mm)
        elif (mm == "" and m != "" and n != ""):
            result = calcmm(n, m)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def n(t):
    result = 'n = 0 mol'
    st.latex(r"n = \frac{m}{M}")
    if t == "Quantidade (mol)":
        result = 'n = 0 mol'
        n = ""
        m = st.number_input("Massa (g)", format="%g" , step=1.0)
        mm = st.number_input("Massa molar (g/mol)", format="%g" , step=1.0)
    elif t == "Massa (g)":
        result = 'm = 0 g'
        m = ""
        n = st.number_input("Quantidade (mol)", format="%g" , step=1.0)
        mm = st.number_input("Massa molar (g/mol)", format="%g" , step=1.0)
    elif t == "Massa molar (g/mol)":
        result = 'M = 0 g/mol'
        mm = ""
        n = st.number_input("Quantidade (mol)", format="%g" , step=1.0)
        m = st.number_input("Massa molar (g/mol)", format="%g" , step=1.0)
    if st.button("Calcular"):
         result = calc(n, m, mm)
    st.title(result)