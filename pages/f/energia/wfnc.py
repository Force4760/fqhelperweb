import streamlit as st

def calcE(f, i):
    e = f - i
    return f"Wfnc = {e} J"
      

def calcf(e, i):
    f = e + i
    return f'Emf = {f} J'

def calci(e, f):
    i = - e + f
    return f"Emi = {i} J"

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


def wfnc(t):
    result = 'Wfnc = 0 J'
    st.latex(r"W_{Fnc} = \Delta E_m")
    if t == "Trabalho das forças não conservativas (J)":
        result = 'Wfnc = 0 J'
        e = ""
        f = st.number_input("Energia mecânica final (J)", format="%g" , step=1.0)
        i = st.number_input("Energia mecânica inicial (J)", format="%g" , step=1.0)
    elif t == "Energia mecânica final (J)":
        result = "Emf = 0 J"
        f = ""
        e = st.number_input("Trabalho das forças não conservativas (J)", format="%g" , step=1.0)
        i = st.number_input("Energia mecânica inicial (J)", format="%g" , step=1.0)
    elif t == "Energia mecânica inicial (J)":
        result = "Emi = 0 J"
        i = ""
        e = st.number_input("Trabalho das forças não conservativas (J)", format="%g" , step=1.0)
        f = st.number_input("Energia mecânica final (J)", format="%g" , step=1.0)
    if st.button("Calcular"):
         result = calc(e, f, i)
    st.title(result)