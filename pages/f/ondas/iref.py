import streamlit as st

def calcn (v ):
    n = 3e8 / v
    return f"n = {n}"

def calcv (n ):
    v = 3e8 / n
    return f"v = {v} m/s"


def calc(n ,v ):
    try:
        if (n == "" and v != ""):
            result = calcn (v )
        elif (v == "" and n != ""):
            result = calcv (n )
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def n(t):
    result = 'n = 0'
    st.latex(r"n = \frac{c}{v}")
    if t == "Índice de refração":
        result = 'n = 0'
        n = ""
        v = st.number_input("Velocidade (m/s)", format="%g" , step=1.0)
    elif t == "Velocidade (m/s)":
        result = "v = 0 m/s"
        v = ""
        n = st.number_input("Índice de refração", format="%g" , step=1.0)
    if st.button("Calcular"):
         result = calc(n , v )
    st.title(result)