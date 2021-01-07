import streamlit as st

def calcE(f, i):
    e = f - i
    return f"W = {e} J"
      

def calcf(e, i):
    f = e + i
    return f'Ecf = {f} J'

def calci(e, f):
    i = - e + f
    return f"Eci = {i} J"

def calc(e, f, i):
    try:
        if (e == "" and f != "" and i != ""):
            result = calcE(f, i)
        elif (f == "" and i != "" and e != ""):
            result = calcf(e, i)
        elif (i == "" and f != "" and e != ""):
            result = calci(e, f)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def tec(t):
    result = 'Em = 0 J'
    st.latex(r"W = \Delta E_c")
    if t == "Trabalho (J)":
        result = 'W = 0 J'
        e = ""
        f = st.number_input("Energia cinética final (J)", format="%g" , step=1.0)
        i = st.number_input("Energia cinética inicial (J)", format="%g" , step=1.0)
    elif t == "Energia cinética inicial (J)":
        result = "Ecf = 0 J"
        f = ""
        e = st.number_input("Trabalho (J)", format="%g" , step=1.0)
        i = st.number_input("Energia cinética inicial (J)", format="%g" , step=1.0)
    elif t == "Energia cinética inicial (J)":
        result = "Eci = 0 J"
        i = ""
        e = st.number_input("Trabalho (J)", format="%g" , step=1.0)
        f = st.number_input("Energia cinética final (J)", format="%g" , step=1.0)
    if st.button("Calcular"):
         result = calc(e, f, i)
    st.title(result)