import streamlit as st

def calcn(mol):
    n =  mol * 6.02e23
    return f"N = {n}"

def calcmol(n):
    mol = n / 6.02e23
    return f"n = {mol} mol"

def calc(n,mol):
    try:
        if (n == "" and mol != ""):
            result = calcn(mol)
        elif (mol == "" and n != ""):
            result = calcmol(n)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def nump(t):
    result = "N = 0"
    st.latex(r"N = n \times N_A")
    if t == "N de partículas":
        result = 'N = 0'
        n = ""
        mol = st.number_input("Qunatidade (mol)", format="%g" , step=1.0)
    elif t == "Quantidade (mol)":
        result = 'n = 0 mol'
        mol = ""
        n = st.number_input("N de partículas", format="%g" , step=1.0)
    if st.button("Calcular"):
         result = calc(n, mol)
    st.title(result)