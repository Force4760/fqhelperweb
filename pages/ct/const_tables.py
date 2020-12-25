import streamlit as st
from pages.ct.parts.tp import tp
from pages.ct.parts.ioes import ions_table
from pages.ct.parts.elig import elig_table
from pages.ct.parts.dens import den_table
from pages.ct.parts.ka import ka_table
from pages.ct.parts.kb import kb_table
from pages.ct.parts.seleox import ox_table
from pages.ct.parts.selered import red_table
tables = ["Tabela Periódica", "Iões", "Energias de Ligação", "Densidade", "Acidez (Ka)", "Basicidade (Kb)", "Oxidantes", "Redutores", "Solubilidades", "Produto de Solubilidade", "Velocidade", "Resistividade", "Capacidade Térmica", "Δhf", "Δhv", "Índice de refração", "Constantes Físicas"]


def table_const():
    st.title("Constantes e Tabelas")
    t = st.selectbox("", tables)
    if t == "Tabela Periódica":
        tp()
    elif t == "Iões":
        ions_table()
    elif t == "Energias de Ligação":
        elig_table()
    elif t == "Densidade":
        den_table()
    elif t == "Acidez (Ka)":
        ka_table()
    elif t == "Basicidade (Kb)":
        kb_table()
    elif t == "Oxidantes":
        ox_table()
    elif t == "Redutores":
        red_table()

    