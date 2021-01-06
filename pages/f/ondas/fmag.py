import streamlit as st
import math

def calcf(b, a, cos, u):
    if u == "º":
        if cos == 90:
            f = b * a * 0
        else:
            f = b * a * math.cos(math.radians(cos))
    elif u == "rad":
        f = b * a * math.cos(cos)
    return f"ϕ = {f} Wb"

def calcb(f, a, cos, u):
    if u == "º":
        if cos == 90:
            b = f / (a * 0)
        else:
            b = f / (a * math.cos(math.radians(cos)))
    elif u == "rad":
        b = f / (a * math.cos(cos))
    return f"B = {b} T"

def calca(f, b, cos, u):
    if u == "º":
        if cos == 90:
            a = f / (b * 0)
        else:
            a = f / (b * math.cos(math.radians(cos)))
    elif u == "rad":
        a = f / (b * math.cos(cos))
    return f"A = {a} m²"

def calccos(f, b, a, u):
    if u == "º":
        cos = f / (b * a)
        cos = math.degrees(math.acos(cos))
    elif u == "rad":
        cos = f / (b * a)
        cos = math.acos(cos)
    return f"α = {cos} {u}"

def calc(f, b, a, cos, u):
    try:
        if (f == "" and b != "" and a != "" and cos != ""):
            result = calcf(b, a, cos, u)
        elif (f != "" and b == "" and a != "" and cos != ""):
            result = calcb(f, a, cos, u)
        elif (f != "" and b != "" and a == "" and cos != ""):
            result = calca(f, b, cos, u)
        elif (f != "" and b != "" and a != "" and cos == ""):
            result = calccos(f, b, a, u)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def fmag(t):
    result = 'ϕ = 0 Wb'
    u = st.radio("",["Ângulo em graus", "Ângulo em radianos"])
    st.latex(r"\Phi = B \times A cos(\alpha)")
    if u == "Ângulo em graus":
        u = "º"
    else:
        u = "rad"
    if t == "Fluxo magnético (Wb)":
        result = 'ϕ = 0 Wb'
        f =  ""
        b = st.number_input("Campo magnético (T)", format="%g" , step=1.0)
        a = st.number_input("Área (m²)", format="%g" , step=1.0)
        cos = st.number_input(f"Ângulo α ({u})", format="%g" , step=1.0)
    elif t == "Campo magnético (T)":
        result = 'B = 0 T'
        f =  st.number_input("Fluxo magnético (Wb)", format="%g" , step=1.0)
        b = ""
        a = st.number_input("Área (m²)", format="%g" , step=1.0)
        cos = st.number_input(f"Ângulo α ({u})", format="%g" , step=1.0)
    elif t == "Área (m²)":
        result = 'A = 0 m²'
        f =  st.number_input("Fluxo magnético (Wb)", format="%g" , step=1.0)
        b = st.number_input("Campo magnético (T)", format="%g" , step=1.0)
        a = ""
        cos = st.number_input(f"Ângulo α ({u})", format="%g" , step=1.0)
    elif t == "Ângulo α":
        result = f'α = 0 {u}'
        f =  st.number_input("Fluxo magnético (Wb)", format="%g" , step=1.0)
        b = st.number_input("Campo magnético (T)", format="%g" , step=1.0)
        a = st.number_input("Área (m²)", format="%g" , step=1.0)
        cos = ""
    if st.button("Calcular"):
         result = calc(f, b, a, cos, u)
    st.title(result)