from pages.ct.fun import table
import streamlit as st
den = ['Gelo: 0.90 ',
       'Alumínio: 2.70 ',
       'Zinco: 7.13 ',
       'Ferro: 7.87 ',
       'Níquel: 8.90 ',
       'Cobre: 8.90 ',
       'Prata: 10.50 ',
       'Chumbo: 11.35 ',
       'Mercúrio: 13.50 ',
       'Ouro: 19.32 ',
       'Etanol: 0.79 ',
       'Parafina: 0.80 ',
       'Água: 1.00 ',
       'Glicerina: 1.30 ',
       'Hidrogénio: 0.000090 ',
       'Hélio: 0.00018 ',
       'Ar: 0.0013 ',
       'Oxigénio: 0.0014'
       'Gelo: 0.90 ',
       'Alumínio: 2.70 ',
       'Zinco: 7.13 ',
       'Ferro: 7.87 ',
       'Níquel: 8.90 ',
       'Cobre: 8.90 ',
       'Prata: 10.50 ',
       'Chumbo: 11.35 ',
       'Mercúrio: 13.50 ',
       'Ouro: 19.32 ',
       'Etanol: 0.79 ',
       'Parafina: 0.80 ',
       'Água: 1.00 ',
       'Glicerina: 1.30 ',
       'Hidrogénio: 0.000090 ',
       'Hélio: 0.00018 ',
       'Ar: 0.0013 ',
       'Oxigénio: 0.0014']

def den_table():
    st.title("Unidades: g/cm³")
    table(den)