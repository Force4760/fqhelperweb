import streamlit as st

def calccn(n, v):
    cn = n / v
    return f"cn = {cn} mol/dm³"

def calcv(n, cn):
    v = n / cn
    return f"V = {v} dm³"

def calcn(cn, v):
    n = v * cn
    return f"n = {n} mol"

def calc(cn,n,v):
    try:
        if (cn == "" and v != "" and n != ""):
            result = calccn(n, v)
        elif (v == "" and n != "" and cn != ""):
            result = calcv(n, cn)
        elif (n == "" and v != "" and cn != ""):
            result = calcn(cn, v)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def cn(t):
    result = 'c = 0 mol/dm³'
    st.latex(r"c = \frac{n}{V}")
    if t == "Concentração (mol/dm³)":
        result = 'c = 0 g/mol'
        cn = ""
        v = st.number_input("Volume (dm³)", format="%g" , step=1.0)
        n = st.number_input("Quantidade (mol)", format="%g" , step=1.0)
    elif t == "Volume (dm³)":
        result = "V = 0 dm³"
        v = ""
        cn = st.number_input("Concentração (mol/dm³)", format="%g" , step=1.0)
        n = st.number_input("Quantidade (mol)", format="%g" , step=1.0)
    elif t == "Quantidade (mol)":
        result = "n = 0 mol"
        n = ""
        cn = st.number_input("Concentração (mol/dm³)", format="%g" , step=1.0)
        v = st.number_input("Volume (dm³)", format="%g" , step=1.0)
    if st.button("Calcular"):
         result = calc(cn, n, v)
    st.title(result)