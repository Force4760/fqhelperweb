import streamlit as st
import math
def calcF(m, a):
    f = m * a
    return f"f = {f} N"
      

def calcM(f, a):
    m = f / a
    return f'm = {m} Kg'

def calcA(f, m):
    a = f / m
    return f"a = {a} m/s²"

def calc(f, m, a):
    try:
        if (f == "" and m != "" and a != ""):
            result = calcF(m, a)
        elif (m == "" and f != "" and a != ""):
            result = calcM(f, a)
        elif (a == "" and f != "" and m != ""):
            result = calcA(f, m)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def fma(t):
    result = 'F = 0 N'
    st.latex(r"F = m a")
    if t == "Força (N)":
        result = 'F = 0 N'
        f = ""
        m = st.number_input("Massa (Kg)", format="%g" , step=1.0)
        a = st.number_input("Aceleração (m/s²)", format="%g" , step=1.0)
    elif t == "Massa (Kg)":
        result = "m = 0 Kg"
        f = st.number_input("Força (N)", format="%g" , step=1.0)
        m = ""
        a = st.number_input("Aceleração (m/s²)", format="%g" , step=1.0)
    elif t == "Aceleração (m/s²)":
        result = "a = 0 m/s²"
        f = st.number_input("Força (N)", format="%g" , step=1.0)
        m = st.number_input("Massa (Kg)", format="%g" , step=1.0)
        a = ""
    if st.button("Calcular"):
         result = calc(f, m, a)
    st.title(result)