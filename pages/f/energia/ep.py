import streamlit as st

def calcE(m, h):
    e = m * 9.81 * h
    return f"Ep = {e} J"
      

def calcM(e, h):
    m = e / (9.81 * h)
    return f'm = {m} g'

def calcH(e, m):
      h = e / (m * 9.81)
      return f"h = {h} m"

def calc(e, m, h):
    try:
        if (e == "" and m != "" and h != ""):
            result = calcE(m, h)
        elif (m == "" and h != "" and e != ""):
            result = calcM(e, h)
        elif (h == "" and m != "" and e != ""):
            result = calcH(e, m)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def ep(t):
    result = 'Ep = 0 J'
    st.latex(r"E_p = m g h (g = 9.81 m/s²)")
    if t == "Energia potencial (J)":
        result = 'Ep = 0 J'
        e = ""
        m = st.number_input("Massa (g)", format="%g" , step=1.0)
        h = st.number_input("Altura (m)", format="%g" , step=1.0)
    elif t == "Massa (g)":
        result = "m = 0 g"
        m = ""
        e = st.number_input("Energia cinética (J)", format="%g" , step=1.0)
        h = st.number_input("Altura (m)", format="%g" , step=1.0)
    elif t == "Altura (m)":
        result = "h = 0 m"
        h = ""
        e = st.number_input("Energia cinética (J)", format="%g" , step=1.0)
        m = st.number_input("Massa (g)", format="%g" , step=1.0)
    if st.button("Calcular"):
         result = calc(e, m, h)
    st.title(result)