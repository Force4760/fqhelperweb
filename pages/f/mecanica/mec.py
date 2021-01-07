import streamlit as st
from pages.f.mecanica.ac1 import ac1
from pages.f.mecanica.ac2 import ac2
from pages.f.mecanica.am import am
from pages.f.mecanica.eqp import eqp
from pages.f.mecanica.eqv import eqv
from pages.f.mecanica.fg import fg
from pages.f.mecanica.fma import fma
from pages.f.mecanica.rm import rm
from pages.f.mecanica.v import v
from pages.f.mecanica.vang1 import vang1
from pages.f.mecanica.vang2 import vang2
from pages.f.mecanica.vm import vm
mec = ["Aceleração Centrípeta 1", "Aceleração Centrípeta 2", "Aceleração Média", "Equação das Posições", "Equação das Velocidades", "Força Gravítica", "Força Resultante", "Rapidez Média", "Velocidade", "Velocidade média", "Velocidade Angular 1", "Velocidade Angular 2"]
def me():
    cal = ["Aceleração Centrípeta (m/s²)", "Velocidade (m/s)", "Raio (m)"]
    cols = st.beta_columns(2)
    q = cols[0].selectbox("Fórmula", mec)
    if q == "Aceleração Centrípeta 1":
        cal = ["Aceleração Centrípeta (m/s²)", "Velocidade (m/s)", "Raio (m)"]
        c = cols[1].selectbox("A Calcular", cal)
        ac1(c)
    elif q == "Aceleração Centrípeta 2":
        cal = ["Aceleração Centrípeta (m/s²)", "Velocidade Angular (rad/s)", "Raio (m)"]
        c = cols[1].selectbox("A Calcular", cal)
        ac2(c)
    elif q == "Aceleração Média":
        cal = ["Aceleração Centrípeta (m/s²)", "Variação da Velocidade (m/s)", "Variação do Tempo (s)"]
        c = cols[1].selectbox("A Calcular", cal)
        am(c)
    elif q == "Equação das Posições":
        cal = ["Posição (m)", "Posição inicial (m)", "Velocidade inicial (m/s)", "Aceleração (m/s²)", "Tempo (s)"]
        c = cols[1].selectbox("A Calcular", cal)
        eqp(c)
    elif q == "Equação das Velocidades":
        cal = ["Velocidade (m/s)", "Velocidade inicial (m/s)", "Aceleração (m/s²)", "Tempo (s)"]
        c = cols[1].selectbox("A Calcular", cal)
        eqv(c)
    elif q == "Força Gravítica":
        cal = ["Força gravítica (N)", "Massa 1 (Kg)", "Massa 2 (Kg)", "Raio (m)"]
        c = cols[1].selectbox("A Calcular", cal)
        fg(c)
    elif q == "Força Resultante":
        cal = ["Força (N)", "Massa (Kg)", "Aceleração (m/s²)",]
        c = cols[1].selectbox("A Calcular", cal)
        fma(c)
    elif q == "Rapidez Média":
        cal = ["Rapidez Média (m/s)", "Distância Percorrida (m)", "Variação do Tempo (s)"]
        c = cols[1].selectbox("A Calcular", cal)
        rm(c)
    elif q == "Velocidade":
        cal = ["Velocidade (m/s)", "Velocidade Angular (rad/s)", "Raio (m)"]
        c = cols[1].selectbox("A Calcular", cal)
        v(c)
    elif q == "Velocidade média":
        cal = ["Velocidade Média (m/s)", "Deslocamento (m)", "Variação do Tempo (s)"]
        c = cols[1].selectbox("A Calcular", cal)
        vm(c)
    elif q == "Velocidade Angular 1":
        cal = ["Velocidade Angular (rad/s)", "Período (s)"]
        c = cols[1].selectbox("A Calcular", cal)
        vang1(c)
    elif q == "Velocidade Angular 2":
        cal = ["Velocidade Angular (rad/s)", "Frequência (Hz)"]
        c = cols[1].selectbox("A Calcular", cal)
        vang2(c)