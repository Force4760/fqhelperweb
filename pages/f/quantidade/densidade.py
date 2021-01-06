import streamlit as st



def calcp(m,v):
    p = m / v
    return f'ρ = {p} g/cm³'


def calcm(p,v):
      m = p * v
      return f'm = {m} g'

def calcv(p,m):
      v = m / p
      return f'V = {v} cm³'
  
def calc(p,m,v):
    try:
        if (p == "" and m != "" and v != ""):
            result = calcp(m,v)
        elif (m == "" and v != "" and p != ""):
            result = calcm(p,v)
        elif (v == "" and p != "" and m != ""):
            result = calcv(p,m)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result
        
def densidade(t):
    result = 'ρ = 0 g/cm³'
    st.latex(r'\rho = \frac{m}{V}')
    if t == "Densidade (g/cm³)":
        result = 'ρ = 0 g/cm³'
        p = ""
        m = st.number_input("Massa (g)", format="%g" , step=1.0)
        v = st.number_input("Volume (cm³)", format="%g" , step=1.0)
    elif t == "Massa (g)":
        result = 'm = 0 g'
        m = ""
        p = st.number_input("Densidade (g/cm³)", format="%g" , step=1.0)
        v = st.number_input("Volume (cm³)", format="%g" , step=1.0)
    elif t == "Volume (cm³)":
        result = 'V = 0 cm³'
        v = ""
        p = st.number_input("Densidade (g/cm³)", format="%g" , step=1.0)
        m = st.number_input("Massa (g)", format="%g" , step=1.0)
    if st.button("Calcular"):
         result = calc(p, m, v)
    st.title(result)








