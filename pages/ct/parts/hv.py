import streamlit as st
from pages.ct.fun import table

hv = ['Água: 2,26 × 10³',
      'Alumínio: 1,14 × 10⁴',
      'Chumbo: 8,70 × 10²',
      'Cobre: 5,06 × 10³',
      'Enxofre: 3,26 × 10²',
      'Etanol: 8,54 × 10²',
      'Hélio: 2,09 × 10',
      'Hidrogénio: 5,55 × 10²',
      'Mercúrio: 2,96 × 10²',
      'Nitrogénio: 2,01 × 10²',
      'Ouro: 1,58 × 10³',
      'Oxigénio: 2,13 × 10²',
      'Prata: 2,33 × 10³']


def hv_table():
    st.title("Unidades: KJ/Kg")
    table(hv)
