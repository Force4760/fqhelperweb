import streamlit as st

def calcE(q, w):
    e = q + w
    return f"ΔU = {e} J"
      

def calcq(e, w):
    q = e - w
    return f'Q = {q} J'

def calcw(e, q):
    w = e - q
    return f"W = {w} J"

def calc(e, q, w):
    try:
        if (e == "" and q != "" and w != ""):
            result = calcE(q, w)
        elif (q == "" and w != "" and e != ""):
            result = calcq(e, w)
        elif (w == "" and q != "" and e != ""):
            result = calcw(e, q)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def eint(t):
    result = 'ΔU = 0 J'
    st.latex(r"\Delta U = W + Q")
    if t == "Energia interna (J)":
        result = 'ΔU = 0 J'
        e = ""
        q = st.number_input("Calor (J)", format="%g" , step=1.0)
        w = st.number_input("Trabalho (J)", format="%g" , step=1.0)
    elif t == "Calor (J)":
        result = "Q = 0 J"
        q = ""
        e = st.number_input("Energia interna (J)", format="%g" , step=1.0)
        w = st.number_input("Trabalho (J)", format="%g" , step=1.0)
    elif t == "Trabalho (J)":
        result = "W = 0 J"
        w = ""
        e = st.number_input("Energia interna (J)", format="%g" , step=1.0)
        q = st.number_input("Calor (J)", format="%g" , step=1.0)
    if st.button("Calcular"):
         result = calc(e, q, w)
    st.title(result)