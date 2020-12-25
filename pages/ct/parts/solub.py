from pages.ct.fun import table
import streamlit as st
solub = ['PbBr₂: 1.2 × 10⁻²',
         'MgBr₂: 2.7 ',
         'KBr: 5.5',
         'AgBr: 7.1 × 10⁻⁷',
         'NaBr: 8.8',
         'BaCO₃: 1.0 × 10⁻⁴',
         'CaCO₃: 1.1 × 10⁻⁴',
         'PbCl₂: 1.6 × 10⁻²',
         'MgCl₂: 5.7',
         'KCl: 4.7',
         'AgCl: 1.3 × 10⁻⁵',
         'NaCl: 6.1',
         'KI: 8.7',
         'AgI: 8.9 × 10⁻⁹',
         'NaI: 12.0',
         'Ba(NO₃)₂: 0.33',
         'Ca(NO₃)₂: 21.0',
         'KNO₃: 3.1',
         'BaSO₄: 1.1 × 10⁻⁵',
         'CaSO₄: 5.0 × 10⁻³',
         'Na₂SO₄: 1.1',
         'PbS: 1.0 × 10⁻¹⁴',
         'Ag₂S: 1.1 × 10⁻¹⁷']

def solub_table():
    st.title("Unidades: mol/dm³")
    table(solub)