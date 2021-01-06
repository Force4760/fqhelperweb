import streamlit as st

def calccm(m, v):
    cm = m / v
    return f"Cm = {cm} g/dm³"

def calcv(m, cm):
    v = m / cm
    return f"V = {v} dm³"

def calcm(cm, v):
    m = v * cm
    return f"m = {m} g"

def calc(cm,m,v):
    try:
        if (cm == "" and v != "" and m != ""):
            result = calccm(m, v)
        elif (v == "" and m != "" and cm != ""):
            result = calcv(m, cm)
        elif (m == "" and v != "" and cm != ""):
            result = calcm(cm, v)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def cm(t):
    result = 'cm = 0 g/dm³'
    st.latex(r"c_m = \frac{m}{V}")
    if t == "Concentração mássica (g/dm³)":
        result = 'cm = 0 g/dm³'
        cm = ""
        v = st.number_input("Volume (dm³)", format="%g" , step=1.0)
        m = st.number_input("Massa (g)", format="%g" , step=1.0)
    elif t == "Volume (dm³)":
        result = "V = 0 dm³"
        v = ""
        cm = st.number_input("Concentração mássica (g/dm³)", format="%g" , step=1.0)
        m = st.number_input("Massa (g)", format="%g" , step=1.0)
    elif t == "Massa (g)":
        result = "m = 0 g"
        m = ""
        cm = st.number_input("Concentração mássica (g/dm³)", format="%g" , step=1.0)
        v = st.number_input("Volume (dm³)", format="%g" , step=1.0)
    if st.button("Calcular"):
         result = calc(cm, m, v)
    st.title(result)