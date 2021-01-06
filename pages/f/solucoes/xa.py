import streamlit as st

def calcxa(na , nt ):
    xa = na / nt
    return f"X = {xa}"

def calcnt(na , xa ):
    nt = na / xa
    return f"nt = {nt} mol"

def calcna(xa , nt ):
    na = nt * xa
    return f"na = {na} mol"

def calc(xa ,na ,nt ):
    try:
        if (xa == "" and nt != "" and na != ""):
            result = calcxa(na , nt )
        elif (nt == "" and na != "" and xa != ""):
            result = calcnt(na , xa )
        elif (na == "" and nt != "" and xa != ""):
            result = calcna(xa , nt )
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def xa(t):
    result = 'X = 0'
    st.latex(r"X = \frac{n_a}{n_t}")
    if t == "Fração molar":
        result = 'X = 0'
        xa = ""
        nt = st.number_input("Quantidade total (mol)", format="%g" , step=1.0)
        na = st.number_input("Quantidade da amostra (mol)", format="%g" , step=1.0)
    elif t == "Quantidade total (mol)":
        result = "nt = 0 mol"
        nt = ""
        xa = st.number_input("Fração molar", format="%g" , step=1.0)
        na = st.number_input("Quantidade da amostra (mol)", format="%g" , step=1.0)
    elif t == "Quantidade da amostra (mol)":
        result = "na = 0 mol"
        na = ""
        xa = st.number_input("Fração molar", format="%g" , step=1.0)
        nt = st.number_input("Quantidade total (mol)", format="%g" , step=1.0)
    if st.button("Calcular"):
         result = calc(xa , na , nt )
    st.title(result)