import streamlit as st
import math

def calcn1(sen1, n2, sen2, u):
    if u == "º":
        n1 = n2 * math.cos(math.radians(sen2)) / math.cos(math.radians(sen1))
    elif u == "rad":
        n1 = n2 * math.cos(sen2) / math.cos(sen1)
    return f"n1 = {n1}"

def calcsen1(n1, n2, sen2, u):
    if u == "º":
        sen1 = n2 * math.cos(math.radians(sen2)) / n1
        sen1 = math.degrees(math.acos(sen1))
    elif u == "rad":
        sen1 = n2 * math.cos(sen2) / n1
        sen1 = math.acos(sen1)
    return f"α1 = {sen1} {u}"

def calcn2(n1, sen1, sen2, u):
    if u == "º":
        n2 = n1 * math.cos(math.radians(sen1)) / math.cos(math.radians(sen2))
    elif u == "rad":
        n2 = n1 * math.cos(sen1) / math.cos(sen2)
    return f"n2 = {n2}"

def calcsen2(n1, sen1, n2, u):
    if u == "º":
        sen2 = n1 * math.cos(math.radians(sen1)) / n2
        sen2 = math.degrees(math.acos(sen2))
    elif u == "rad":
        sen2 = n1 * math.cos(sen1) / n2
        sen2 = math.acos(sen2)
    return f"α2 = {sen2} {u}"


def calc(n1, sen1, n2, sen2, u):
    try:
        if (n1 == "" and sen1 != "" and n2 != "" and sen2 != ""):
            result = calcn1(sen1, n2, sen2, u)
        elif (n1 != "" and sen1 == "" and n2 != "" and sen2 != ""):
            result = calcsen1(n1, n2, sen2, u)
        elif (n1 != "" and sen1 != "" and n2 == "" and sen2 != ""):
            result = calcn2(n1, sen1, sen2, u)
        elif (n1 != "" and sen1 != "" and n2 != "" and sen2 == ""):
            result = calcsen2(n1, sen1, n2, u)
        else:
            result = 'Impossível'
    except:
        result = 'Impossível'
    return result


def snell(t):
    result = 'n1 = 0'
    u = st.radio("",["Ângulo em graus", "Ângulo em radianos"])
    st.latex(r"n_1 \times sen(\alpha_1) = n_2 \times sen(\alpha_2)")
    if u == "Ângulo em graus":
        u = "º"
    else:
        u = "rad"
    if t == "Índice de refração 1":
        result = 'n1 = 0'
        n1 = ""
        sen1 = st.number_input(f"Ângulo α1 ({u})", format="%g" , step=1.0)
        n2 = st.number_input("Índice de refração 2", format="%g" , step=1.0)
        sen2 = st.number_input(f"Ângulo α2 ({u})", format="%g" , step=1.0)
    elif t == "Ângulo α1":
        result = f'α1 = 0 {u}'
        n1 = st.number_input("Índice de refração 1", format="%g" , step=1.0)
        sen1 = ""
        n2 = st.number_input("Índice de refração 2", format="%g" , step=1.0)
        sen2 = st.number_input(f"Ângulo α ({u})", format="%g" , step=1.0)
    elif t == "Índice de refração 2":
        result = 'n2 = 0'
        n1 = st.number_input("Índice de refração 1", format="%g" , step=1.0)
        sen1 = st.number_input(f"Ângulo α1 ({u})", format="%g" , step=1.0)
        n2 = ""
        sen2 = st.number_input(f"Ângulo α2 ({u})", format="%g" , step=1.0)
    elif t == "Ângulo α2":
        result = f'α2 = 0 {u}'
        n1 = st.number_input("Índice de refração 1", format="%g" , step=1.0)
        sen1 = st.number_input(f"Ângulo α1 ({u})", format="%g" , step=1.0)
        n2 = st.number_input("Índice de refração 2", format="%g" , step=1.0)
        sen2 = ""
    if st.button("Calcular"):
         result = calc(n1, sen1, n2, sen2)
    st.title(result)