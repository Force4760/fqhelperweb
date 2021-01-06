import streamlit as st
import math


def calcV(v0, a, t):
    v =  v0 + a * t
    return f"v = {v} m/s"

def calcV0(v, a, t):
    v0 = v - (a * t)
    return f"v₀ = {v0} m/s"

def calcA(v, v0, t):
    a = (v - v0) / t
    return f"a = {a} m/s²"

def calcT(v, v0, a):
    t = (v - v0) / a
    return f"t = {t} s"


def calc(v, v0, a, t):
    try:
        if (v == "" and v0 != "" and a != "" and t != ""):
            result = calcV(v0, a, t)
        elif (v0 == "" and v != "" and a != "" and t != ""):
            result = calcV0(v, a, t)
        elif (a == "" and v != "" and v0 != "" and t != ""):
            result = calcA(v, v0, t)
        elif (t == "" and v != "" and a != "" and v0 != ""):
            result = calcT(v, v0, a)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def eqv(b):
    result = 'v = 0 m/s'
    st.latex(r"v(t) = v_0 + a t")
    if b == "Velocidade (m/s)":
        result = 'v = 0 m/s'
        v = ""
        v0 = st.number_input("Velocidade inicial (m/s)", format="%g" , step=1.0)
        a = st.number_input("Aceleração (m/s²)", format="%g" , step=1.0)
        t = st.number_input("Tempo (s)", format="%g" , step=1.0)
    elif b == "Velocidade inicial (m/s)":
        result = 'v₀ = 0 m/s'
        v = st.number_input("Velocidade (m/s)", format="%g" , step=1.0)
        v0 = ""
        a = st.number_input("Aceleração (m/s²)", format="%g" , step=1.0)
        t = st.number_input("Tempo (s)", format="%g" , step=1.0)
    elif b == "Aceleração (m/s²)":
        result = 'a = 0 m/s²'
        v = st.number_input("Velocidade (m/s)", format="%g" , step=1.0)
        v0 = st.number_input("Velocidade inicial (m/s)", format="%g" , step=1.0)
        a = ""
        t = st.number_input("Tempo (s)", format="%g" , step=1.0)
    elif b == "Tempo (s)":
        result = 't = 0 s'
        v = st.number_input("Velocidade (m/s)", format="%g" , step=1.0)
        v0 = st.number_input("Velocidade inicial (m/s)", format="%g" , step=1.0)
        a = st.number_input("Aceleração (m/s²)", format="%g" , step=1.0)
        t = ""
    if st.button("Calcular"):
         result = calc(v, v0, a, t)
    st.title(result)

