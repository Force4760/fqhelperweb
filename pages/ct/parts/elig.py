from pages.ct.fun import table
import streamlit as st
elig = ['Br–Br: 192.5 ', 'Br–C: 276 ', 'Br–H: 366.1 ', 'C–C: 347 ', 'C=C: 612 ', 'C≡C: 835 ', 'C–Cl: 338 ', 'C–F: 484 ', 'C–H: 414 ', 'C–I: 238 ', 'C–N: 276 ', 'C=N: 615 ', 'C≡N: 891 ', 'C–O: 360 ', 'C=O: 745 ', 'C–P: 263 ', 'C–S: 255 ', 'C=S: 477 ', 'Cl–Cl: 242.7 ', 'Cl–H: 431.9 ', 'Cl–S: 253 ', 'F–F: 156.9 ', 'F–H: 568.2 ', 'F–O: 190 ', 'H–H: 436.4 ', 'H–I: 298.3 ', 'H–N: 393 ', 'H–O: 460 ', 'H–P: 326 ', 'H–S: 363 ', 'I–I: 151.0 ', 'N–N: 193 ', 'N=N: 418 ', 'N≡N: 944 ', 'N–O: 176 ', 'N–P: 209 ', 'O–O: 157 ', 'O=O: 498.7 ', 'O–P: 502 ', 'O=S: 469 ', 'P–P: 197 ', 'P=P: 489 ', 'S–S: 268 ', 'S=S: 352 ']

def elig_table():
    st.title("Unidades: KJ/mol")
    table(elig)