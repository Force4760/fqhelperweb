import streamlit as st

def calcgp(mp, mt):
    gp = ( mp / mt ) * 100
    return f"G.P. = {gp}%"

def calcmp(gp, mt):
    mp = (gp * mt) / 100
    return f"mp = {mp} g"

def calcmt(gp, mp):
    mt = (mp / gp) * 100
    return f"mt = {mt} g"

def calc(gp,mp,mt):
    try:
        if (gp == "" and mp != "" and mt != ""):
            result = calcgp(mp, mt)
        elif (mp == "" and mt != "" and gp != ""):
            result = calcmp(gp,mt)
        elif (mt == "" and mp != "" and gp != ""):
            result = calcmt(gp, mp)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def gp(t):
    result = 'G.P. = 0%'
    st.latex(r"G.P. = \frac{mp}{mt} \times 100")
    if t == "Grau de pureza (%)":
        result = 'G.P. = 0%'
        gp = ""
        mp = st.number_input("Massa pura (g)", format="%g" , step=1.0)
        mt = st.number_input("Massa total (g)", format="%g" , step=1.0)
    elif t == "Massa pura (g)":
        result = 'mp = 0 g'
        mp = ""
        gp = st.number_input("Grau de pureza (%)", format="%g" , step=1.0)
        mt = st.number_input("Massa total (g)", format="%g" , step=1.0)
    elif t == "Massa total (g)":
        result = 'mt = 0 g'
        mt = ""
        gp = st.number_input("Grau de pureza (%)", format="%g" , step=1.0)
        mp = st.number_input("Massa pura (g)", format="%g" , step=1.0)
    if st.button("Calcular"):
         result = calc(gp, mp, mt)
    st.title(result)