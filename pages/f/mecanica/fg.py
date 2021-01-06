import streamlit as st
import math
def calcF(m1, m2, r):
    g = 0.0000000000667
    f = m1 * m2 * g / (r * r)
    return f"F = {f} N"
      

def calcM1(f, m2, r):
    g = 0.0000000000667
    m1 = f * r * r / (m2 * g)
    return f'm1 = {m1} Kg'

def calcM2(f, m1, r):
    g = 0.0000000000667
    m2 = f * r * r / (m1 * g)
    return f'm2 = {m2} Kg'

def calcR(f, m1, m2):
    g = 0.0000000000667
    r = math.sqrt(g * m1 * m2 / f)
    return f'R = {r} m'

def calc(f, m1, m2, r):
    try:
        if (f == "" and m1 != "" and m2 != "" and r != ""):
            result = calcF(m1, m2, r)
        elif (m1 == "" and f != "" and m2 != "" and r != ""):
            result = calcM1(f, m2, r)
        elif (m2 == "" and m1 != "" and f != "" and r != ""):
            result = calcM2(f, m1, r)
        elif (r == "" and m1 != "" and m2 != "" and f != ""):
            result = calcR(f, m1, m2)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def fg(t):
    result = 'F = 0 N'
    st.latex(r"F = \frac{G m_1 m_2}{R^2}")
    if t == "Força gravítica (N)":
        result = 'F = 0 N'
        f = ""
        m1 = st.number_input("Massa 1 (Kg)", format="%g" , step=1.0)
        m2 = st.number_input("Massa 2 (Kg)", format="%g" , step=1.0)
        r = st.number_input("Raio (m)", format="%g" , step=1.0)
    elif t == "Massa 1 (Kg)":
        result = "m1 = 0 Kg"
        f = st.number_input("Força gravítica (N)", format="%g" , step=1.0)
        m1 = ""
        m2 = st.number_input("Massa 2 (Kg)", format="%g" , step=1.0)
        r = st.number_input("Raio (m)", format="%g" , step=1.0)
    elif t == "Massa 2 (Kg)":
        result = "m2 = 0 Kg"
        f = st.number_input("Força gravítica (N)", format="%g" , step=1.0)
        m1 = st.number_input("Massa 1 (Kg)", format="%g" , step=1.0)
        m2 = ""
        r = st.number_input("Raio (m)", format="%g" , step=1.0)
    elif t == "Raio (m)":
        result = "R = 0 m"
        f = st.number_input("Força gravítica (N)", format="%g" , step=1.0)
        m1 = st.number_input("Massa 1 (Kg)", format="%g" , step=1.0)
        m2 = st.number_input("Massa 2 (Kg)", format="%g" , step=1.0)
        r = ""
    if st.button("Calcular"):
         result = calc(f, m1, m2, r)
    st.title(result)