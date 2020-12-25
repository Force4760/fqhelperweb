import streamlit as st
from pages.ct.fun import table

resis = ['Alumínio: 2.8 × 10⁻⁸',
         'Borracha: 10¹³',
         'Carbono: 3.5 × 10⁻⁵',
         'Constantan: 4.4 × 10⁻⁷',
         'Cobre: 1.7 × 10⁻⁸',
         'Ebonite: 1.5 × 10¹⁴',
         'Enxofre: 10¹⁵',
         'Ferro: 1.0 × 10⁻⁷',
         'Germânio: 4.5 × 10⁻¹',
         'Madeira: 10⁸ a 10¹⁴',
         'Manganina: 4.4 × 10⁻⁷',
         'Nicrómio: 1.0 × 10⁻⁶',
         'Níquel: 6.8 × 10⁻⁸',
         'Prata: 1.6 × 10⁻⁸',
         'Silício: 6.4 × 10²',
         'Tungsténio: 5.6 × 10⁻⁸',
         'Vidro: 10¹⁰ a 10¹⁴']

def resis_table():
    st.title("Unidades: Ω m")
    table(resis)