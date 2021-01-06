import streamlit as st

def calcE(f, i):
    e = - f + i
    return f"Wp = {e} J"
      

def calcf(e, i):
    f = - e + i
    return f'Epf = {f} J'

def calci(e, f):
    i = f + e
    return f"Epi = {i} J"

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


def trabp(t):
    result = 'Wp = 0 J'
    st.latex(r"W_p = \Delta E_p")
    if t == "Trabalho do peso (J)":
        result = 'W = 0 J'
        e = ""
        f = st.number_input("Energia potencial final (J)", format="%g" , step=1.0)
        i = st.number_input("Energia potencial inicial (J)", format="%g" , step=1.0)
    elif t == "Energia potencial final (J)":
        result = "Epf = 0 J"
        f = ""
        e = st.number_input("Trabalho do peso (J)", format="%g" , step=1.0)
        i = st.number_input("Energia potencial inicial (J)", format="%g" , step=1.0)
    elif t == "Energia potencial inicial (J)":
        result = "Epi = 0 J"
        i = ""
        e = st.number_input("Trabalho do peso (J)", format="%g" , step=1.0)
        f = st.number_input("Energia potencial final (J)", format="%g" , step=1.0)
    if st.button("Calcular"):
         result = calc(e, f, i)
    st.title(result)