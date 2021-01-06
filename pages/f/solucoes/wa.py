import streamlit as st

def calcwa(ma , mt ):
    wa = ma / mt
    return f"W = {wa}"

def calcmt(ma , wa ):
    mt = ma / wa
    return f"mt = {mt} g"

def calcma(wa , mt ):
    ma = mt * wa
    return f"ma = {ma} g"

def calc(wa ,ma ,mt ):
    try:
        if (wa == "" and mt != "" and ma != ""):
            result = calcwa(ma , mt )
        elif (mt == "" and ma != "" and wa != ""):
            result = calcmt(ma , wa )
        elif (ma == "" and mt != "" and wa != ""):
            result = calcma(wa , mt )
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def wa(t):
    result = 'W = 0'
    st.latex(r"W = \frac{m_a}{m_t}")
    if t == "Fração mássica":
        result = 'W = 0'
        wa = ""
        mt = st.number_input("Massa total (g)", format="%g" , step=1.0)
        ma = st.number_input("Massa da amostra (g)", format="%g" , step=1.0)
    elif t == "Massa total (g)":
        result = "mt = 0 g"
        mt = ""
        wa = st.number_input("Fração mássica", format="%g" , step=1.0)
        ma = st.number_input("Massa da amostra (g)", format="%g" , step=1.0)
    elif t == "Massa da amostra (g)":
        result = "ma = 0 g"
        ma = ""
        wa = st.number_input("Fração mássica", format="%g" , step=1.0)
        mt = st.number_input("Massa total (g)", format="%g" , step=1.0)
    if st.button("Calcular"):
         result = calc(wa , ma , mt )
    st.title(result)