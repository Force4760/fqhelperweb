import streamlit as st
from pages.ct.fun import table

ctm = ['Aço: 460',
       'Água: 4.18x10³',
       'Água (vapor): 2100',
       'Água do mar: 3890',
       'Alumínio: 900',
       'Ar (p constante): 1000',
       'Ar (v constante)	: 720',
       'Azoto: 1040',
       'Benzeno: 1700',
       'Berílio: 1830',
       'Bronze: 385',
       'Cádmio: 230',
       'Chumbo: 128',
       'Cobre: 386',
       'Estanho: 217',
       'Etanol: 2419',
       'Éter: 2320',
       'Ferro: 450',
       'Gelo: 2090',
       'Glicerina	: 2420',
       'Grafite: 720',
       'Granito: 800',
       'Hélio: 5180',
       'Hidrogénio: 14300',
       'Latão: 393',
       'Madeira: 1700',
       'Mármore: 880',
       'Mercúrio: 140 ',
       'Níquel: 443',
       'Ouro: 129',
       'Oxigénio: 920',
       'Parafina: 2100',
       'Petróleo: 2100',
       'Prata: 234',
       'Tungsténio: 443',
       'Vidro: 837',
       'Zinco: 387 ']

def ctm_table():
    st.title("Unidades: J Kg⁻¹ K⁻¹")
    table(ctm)
