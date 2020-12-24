import streamlit as st

tables = ["Tabela Periódica", "Iões", "Energias de Ligação", "Densidade", "Acidez (Ka)", "Basicidade (Kb)", "Série Eletroquímica", "Solubilidades", "Produto de Solubilidade", "Velocidade", "Resistividade", "Capacidade Térmica", "Δhf", "Δhv", "Índice de refração", "Constantes Físicas"]


def table_const():
    st.title("Constantes e Tabelas")
    t = st.selectbox("", tables)
    st.subheader(t)
    