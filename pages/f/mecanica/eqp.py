import streamlit as st
import math

def calcX(x0, v0, a, t):
    x = x0 + (v0 * t) + (a * t * t) / 2
    return f"x = {x} m"

def calcX0(x, v0, a, t):
    x0 = x - (v0 * t) - (a * t * t) / 2
    return f"x₀ = {x0} m"

def calcV0(x, x0, a, t):
    v0 = ( x - x0 - (a * t * t) / 2 ) / t
    return f"v₀ = {v0} m/s"

def calcA(x, x0, v0, t):
    a = ((x - x0 - (v0 * t)) * 2 ) / (t * t)
    return f"a = {a} m/s²"

def calcT(x, x0, v0, a):
    pa = a / 2
    pb = v0
    pc = x0 - x
    d = (pb * pb) - (4*pa*pc)
    t1 = ( - pb - math.sqrt(d) ) / ( 2 * pa )
    t2 = ( - pb + math.sqrt(d) ) / ( 2 * pa )
    return f"t₁ = {t1} s v t₂ = {t2} s"


def calc(x, x0, v0, a, t):
    try:
        if (x == "" and x0 != "" and v0 != "" and a != "" and t != ""):
            result = calcX(x0, v0, a, t)
        elif (x0 == "" and x != "" and v0 != "" and a != "" and t != ""):
            result = calcX0(x, v0, a, t)
        elif (v0 == "" and x0 != "" and x != "" and a != "" and t != ""):
            result = calcV0(x, x0, a, t)
        elif (a == "" and x0 != "" and x != "" and v0 != "" and t != ""):
            result = calcA(x, x0, v0, t)
        elif (t == "" and x0 != "" and x != "" and a != "" and v0 != ""):
            result = calcT(x, x0, v0, a)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def eqp(b):
    result = 'x = 0 m'
    st.latex(r"x(t) = x_0 + v_0 t + \frac{1}{2} a t^2")
    if b == "Posição (m)":
        result = 'x = 0 m'
        x = ""
        x0 = st.number_input("Posição inicial (m)", format="%g" , step=1.0)
        v0 = st.number_input("Velocidade inicial (m/s)", format="%g" , step=1.0)
        a = st.number_input("Aceleração (m/s²)", format="%g" , step=1.0)
        t = st.number_input("Tempo (s)", format="%g" , step=1.0)
    elif b == "Posição inicial (m)":
        result = 'x₀ = 0 m'
        x = st.number_input("Posição (m)", format="%g" , step=1.0)
        x0 = ""
        v0 = st.number_input("Velocidade inicial (m/s)", format="%g" , step=1.0)
        a = st.number_input("Aceleração (m/s²)", format="%g" , step=1.0)
        t = st.number_input("Tempo (s)", format="%g" , step=1.0)
    elif b == "Velocidade inicial (m/s)":
        result = 'v₀ = 0 m/s'
        x = st.number_input("Posição (m)", format="%g" , step=1.0)
        x0 = st.number_input("Posição inicial (m)", format="%g" , step=1.0)
        v0 = ""
        a = st.number_input("Aceleração (m/s²)", format="%g" , step=1.0)
        t = st.number_input("Tempo (s)", format="%g" , step=1.0)
    elif b == "Aceleração (m/s²)":
        result = 'a = 0 m/s²'
        x = st.number_input("Posição (m)", format="%g" , step=1.0)
        x0 = st.number_input("Posição inicial (m)", format="%g" , step=1.0)
        v0 = st.number_input("Velocidade inicial (m/s)", format="%g" , step=1.0)
        a = ""
        t = st.number_input("Tempo (s)", format="%g" , step=1.0)
    elif b == "Tempo (s)":
        result = 't = 0 s'
        x = st.number_input("Posição (m)", format="%g" , step=1.0)
        x0 = st.number_input("Posição inicial (m)", format="%g" , step=1.0)
        v0 = st.number_input("Velocidade inicial (m/s)", format="%g" , step=1.0)
        a = st.number_input("Aceleração (m/s²)", format="%g" , step=1.0)
        t = ""
    if st.button("Calcular"):
         result = calc(x, x0, v0, a, t)
    st.title(result)

