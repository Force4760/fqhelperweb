import streamlit as st
from pages.ct.fun import table

hf = ['Água: 3,34 × 10²',
      'Alumínio: 3,97 × 10²',
      'Chumbo: 2,45 × 10',
      'Cobre: 1,34 × 10²',
      'Enxofre: 3,81 × 10',
      'Etanol: 1,04 × 10²',
      'Hélio: 5,23',
      'Hidrogénio: 5,80 × 10',
      'Mercúrio: 1,14 × 10',
      'Nitrogénio: 2,55 × 10',
      'Ouro: 6,44 × 10',
      'Oxigénio: 1,38 × 10',
      'Prata: 8,82 × 10']


def hf_table():
    st.title("Unidades: KJ/Kg")
    table(hf)