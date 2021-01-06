import streamlit as st

def calcmm(ma , mt ):
    mm = ma / mt * 100
    return f"(m/m) = {mm}%"

def calcmt(ma , mm ):
    mt = ma / mm * 100
    return f"msolução = {mt} g"

def calcma(mm , mt ):
    ma = mt * mm / 100
    return f"msoluto = {ma} g"

def calc(mm ,ma ,mt ):
    try:
        if (mm == "" and mt != "" and ma != ""):
            result = calcmm(ma , mt )
        elif (mt == "" and ma != "" and mm != ""):
            result = calcmt(ma , mm )
        elif (ma == "" and mt != "" and mm != ""):
            result = calcma(mm , mt )
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def mm(t):
    result = '(m/m) = 0%'
    st.latex(r"(m/m) = \frac{m_{soluto}}{m_{solução}} \times 100")
    if t == "% Massa/Massa":
        result = '(m/m) = 0%'
        mm = ""
        mt = st.number_input("Massa da solução (g)", format="%g" , step=1.0)
        ma = st.number_input("Massa do soluto (g)", format="%g" , step=1.0)
    elif t == "Massa da solução (g)":
        result = "msolução = 0 g"
        mt = ""
        mm = st.number_input("% Massa/Massa", format="%g" , step=1.0)
        ma = st.number_input("Massa do soluto (g)", format="%g" , step=1.0)
    elif t == "Massa do soluto (g)":
        result = "msoluto = 0 g"
        ma = ""
        mm = st.number_input("% Massa/Massa", format="%g" , step=1.0)
        mt = st.number_input("Massa da solução (g)", format="%g" , step=1.0)
    if st.button("Calcular"):
         result = calc(mm , ma , mt )
    st.title(result)