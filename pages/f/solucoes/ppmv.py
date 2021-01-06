import streamlit as st

def calcvv(va , vt ):
    vv = va / vt * 100
    return f"ppm(v) = {vv} ppm"

def calcvt(va , vv ):
    vt = va / vv * 100
    return f"Vsolução = {vt} dm³"

def calcva(vv , vt ):
    va = vt * vv / 100
    return f"Vsoluto = {va} dm³"

def calc(vv ,va ,vt ):
    try:
        if (vv == "" and vt != "" and va != ""):
            result = calcvv(va , vt )
        elif (vt == "" and va != "" and vv != ""):
            result = calcvt(va , vv )
        elif (va == "" and vt != "" and vv != ""):
            result = calcva(vv , vt )
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def ppmv(t):
    result = 'ppm(v) = 0 ppm'
    st.latex(r"ppm(v) = \frac{V_{soluto}}{V_{solução}} \times 10^6")
    if t == "PPM Volume/Volume":
        result = 'ppm(v) = 0 ppm'
        vv = ""
        vt = st.number_input("Volume da solução (dm³)", format="%g" , step=1.0)
        va = st.number_input("Volume do soluto (dm³)", format="%g" , step=1.0)
    elif t == "Volume da solução (dm³)":
        result = "Vsolução = 0 dm³"
        vt = ""
        vv = st.number_input("PPM Volume/Volume", format="%g" , step=1.0)
        va = st.number_input("Volume do soluto (dm³)", format="%g" , step=1.0)
    elif t == "Volume do soluto (dm³)":
        result = "Vsoluto = 0 dm³"
        va = ""
        vv = st.number_input("PPM Volume/Volume", format="%g" , step=1.0)
        vt = st.number_input("Volume da solução (dm³)", format="%g" , step=1.0)
    if st.button("Calcular"):
         result = calc(vv , va , vt )
    st.title(result)