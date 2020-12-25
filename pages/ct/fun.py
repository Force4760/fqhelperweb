import streamlit as st
def table(l):
    search = st.text_input("Procura")
    if search == "":
        for i in l:
            st.header(i)   
    else:
        indices = []
        for i, elem in enumerate(l):
            if search.lower() in elem.lower():
                indices.append(i)
        if indices == []:
            st.header("Desculpa! Não encontramos nada.") 
        else:
            for i in indices:
                st.header(l[i]) 