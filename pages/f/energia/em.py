import streamlit as st

def calcE(c, p):
    e = c + p
    return f"Em = {e} J"
      

def calcc(e, p):
    c = e - p
    return f'Ec = {c} J'

def calcp(e, c):
    p = e - c
    return f"Ep = {p} J"

def calc(e, c, p):
    try:
        if (e == "" and c != "" and p != ""):
            result = calcE(c, p)
        elif (c == "" and p != "" and e != ""):
            result = calcc(e, p)
        elif (p == "" and c != "" and e != ""):
            result = calcp(e, c)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def em(t):
    result = 'Em = 0 J'
    st.latex(r"E_m = E_c + E_p")
    if t == "Energia mecânica (J)":
        result = 'Em = 0 J'
        e = ""
        c = st.number_input("Energia cinética (J)", format="%g" , step=1.0)
        p = st.number_input("Energia potencial (J)", format="%g" , step=1.0)
    elif t == "Energia cinética (J)":
        result = "Ec = 0 J"
        c = ""
        e = st.number_input("Energia mecânica (J)", format="%g" , step=1.0)
        p = st.number_input("Energia potencial (J)", format="%g" , step=1.0)
    elif t == "Energia potencial (J)":
        result = "Ep = 0 J"
        p = ""
        e = st.number_input("Energia mecânica (J)", format="%g" , step=1.0)
        c = st.number_input("Energia cinética (J)", format="%g" , step=1.0)
    if st.button("Calcular"):
         result = calc(e, c, p)
    st.title(result)