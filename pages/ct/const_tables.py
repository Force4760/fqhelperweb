import streamlit as st
from pages.ct.parts.tp import tp
from pages.ct.parts.ioes import ions_table
from pages.ct.parts.elig import elig_table
from pages.ct.parts.dens import den_table
from pages.ct.parts.ka import ka_table
from pages.ct.parts.kb import kb_table
from pages.ct.parts.seleox import ox_table
from pages.ct.parts.selered import red_table
from pages.ct.parts.solub import solub_table
from pages.ct.parts.psol import psol_table
from pages.ct.parts.vel import vel_table
from pages.ct.parts.resis import resis_table
from pages.ct.parts.ctm import ctm_table
from pages.ct.parts.hf import hf_table
from pages.ct.parts.hv import hv_table
from pages.ct.parts.iref import iref_table
from pages.ct.parts.consts import c_table
tables = ["Tabela Periódica", "Iões", "Energias de Ligação", "Densidade", "Acidez (Ka)", "Basicidade (Kb)", "Oxidantes", "Redutores", "Solubilidades", "Produto de Solubilidade", "Velocidade", "Resistividade", "Capacidade Térmica Mássica", "Δhf", "Δhv", "Índice de refração", "Constantes Físicas"]


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
    elif t == "Solubilidades":
        solub_table()
    elif t == "Produto de Solubilidade":
        psol_table()
    elif t == "Velocidade":
        vel_table()
    elif t == "Resistividade":
        resis_table()
    elif t == "Capacidade Térmica Mássica":
        ctm_table()
    elif t == "Δhf":
        hf_table()
    elif t == "Δhv":
        hv_table()
    elif t == "Índice de refração":
        iref_table()
    elif t == "Constantes Físicas":
        c_table()
    