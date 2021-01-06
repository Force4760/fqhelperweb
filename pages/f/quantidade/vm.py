import streamlit as st

def calcvm(v, n):
    vm = v / n
    return f"Vm = {vm} dm³/mol"

def calcv(vm, n):
    v = vm * n
    return f"V = {v} dm³"

def calcn(vm, v):
    n = v / vm
    return f"n = {n} mol"

def calc(vm,v,n):
    try:
        if (vm == "" and v != "" and n != ""):
            result = calcvm(v, n)
        elif (v == "" and n != "" and vm != ""):
            result = calcv(vm,n)
        elif (n == "" and v != "" and vm != ""):
            result = calcn(vm, v)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def vm(t):
    result = 'Vm = 0 dm³/mol'
    st.latex(r"V_m = \frac{V}{n}")
    if t == "Volume molar (dm³/mol)":
        result = 'Vm = 0 dm³/mol'
        vm = ""
        v = st.number_input("Volume (dm³)", format="%g" , step=1.0)
        n = st.number_input("Quantidade (mol)", format="%g" , step=1.0)
    elif t == "Volume (dm³)":
        result = "V = 0 dm³"
        v = ""
        vm = st.number_input("Volume molar (dm³/mol)", format="%g" , step=1.0)
        n = st.number_input("Quantidade (mol)", format="%g" , step=1.0)
    elif t == "Quantidade (mol)":
        result = "n = 0 mol"
        n = ""
        vm = st.number_input("Volume molar (dm³/mol)", format="%g" , step=1.0)
        v = st.number_input("Volume (dm³)", format="%g" , step=1.0)
    if st.button("Calcular"):
         result = calc(vm, v, n)
    st.title(result)