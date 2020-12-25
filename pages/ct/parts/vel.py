import streamlit as st
from pages.ct.fun import table

vel = ['Luz (vácuo): 3 x 10⁸',
       'Luz (ar): 3 x 10⁸',
       'Luz (água): 225407863',
       'Luz (vidro): 199861638',
       'Som (ar): 340',
       'Som (ar 0°C): 331,45',
       'Som (ar 10°C): 337.5',
       'Som (ar 20°C): 343.4',
       'Som (ar 30°C): 349.2',
       'Som (mar): 1532.8',
       'Som (álcool): 1210',
       'Som (chumbo): 1230',
       'Som (mercúrio): 1450',
       'Som (cobre): 3750',
       'Som (betão): 5000',
       'Som (alumínio): 5100',
       'Som (ferro): 5130',
       'Som (granito): 6000',
       'Som (aço): 6000',
       'Som (nitrogénio): 339,3',
       'Som (oxigénio): 317,2',
       'Som (hélio): 927',
       'Som (hidrogénio): 1269.5']

def vel_table():
    st.title("Unidades: m/s")
    table(vel)