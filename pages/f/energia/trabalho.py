import streamlit as st
import math
def calcW(f,d,a, u):
    if u == "º":
        w = f * d * math.cos(math.radians(a))
    elif u == "rad":
        w = f * d * math.cos(a)
    return f"W = {w} J"

def calcF(w,d,a, u):
    if u == "º":
        f = w / (d * math.cos(math.radians(a)))
    elif u == "rad":
        f = w / (d * math.cos(a))
    return f"F = {f} N"

def calcD(w,f,a, u):
    if u == "º":
        d = w / (f * math.cos(math.radians(a)))
    elif u == "rad":
        d = w / (f * math.cos(a))
    return f"d = {d} m"

def calcA(w,d,f, u):
    if u == "º":
        a = w / (d*f)
        a = math.degrees(math.acos(a))
    elif u == "rad":
        a = w / (d*f)
        a = math.acos(a)
    return f"α = {a} {u}"


def calc(w, f, d, a, u):
    try:
        if (w == "" and f != "" and d != "" and a != ""):
            result = calcW(f, d, a, u)
        elif (w != "" and f == "" and d != "" and a != ""):
            result = calcF(w, d, a, u)
        elif (w != "" and f != "" and d == "" and a != ""):
            result = calcD(w, f, a, u)
        elif (w != "" and f != "" and d != "" and a == ""):
            result = calcA(w, f, d, u)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def trabalho(t):
    result = 'W = 0 J'
    st.latex(r"W = F d cos(\alpha)")
    u = st.radio("",["Ângulo em graus", "Ângulo em radianos"])
    if u == "Ângulo em graus":
        u = "º"
    else:
        u = "rad"
    if t == "Trabalho (J)":
        result = 'W = 0 J'
        w = ""
        f = st.number_input("Força (N)", format="%g" , step=1.0)
        d = st.number_input("Deslocamento (m)", format="%g" , step=1.0)
        a = st.number_input("Ângulo α ({u})", format="%g" , step=1.0)
    elif t == "Força (N)":
        result = "F = 0 N"
        w = st.number_input("Trabalho (J)", format="%g" , step=1.0)
        f = ""
        d = st.number_input("Deslocamento (m)", format="%g" , step=1.0)
        a = st.number_input("Ângulo α ({u})", format="%g" , step=1.0)
    elif t == "Deslocamento (m)":
        result = "d = 0 m"
        w = st.number_input("Trabalho (J)", format="%g" , step=1.0)
        f = st.number_input("Força (N)", format="%g" , step=1.0)
        d = ""
        a = st.number_input("Ângulo α ({u})", format="%g" , step=1.0)
    elif t == "Ângulo α1":
        result = f'α1 = 0 {u}'
        w = st.number_input("Trabalho (J)", format="%g" , step=1.0)
        f = st.number_input("Força (N)", format="%g" , step=1.0)
        d = st.number_input("Deslocamento (m)", format="%g" , step=1.0)
        a = ""
    if st.button("Calcular"):
         result = calc(w, f, d, a, u)
    st.title(result)