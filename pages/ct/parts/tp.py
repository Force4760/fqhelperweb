import streamlit as st

elements = ['Hidrogénio','Hélio','Lítio','Berílio','Boro','Carbono','Nitrogénio','Oxigénio','Flúor','Néon','Sódio','Magnésio','Alumínio','Silício','Fósforo','Enxofre','Cloro','Árgon','Potássio','Cálcio','Escândio','Titânio','Vanádio','Crómo','Manganês','Ferro','Cobalto','Níquel','Cobre','Zinco','Gálio','Germânio','Arsénio','Selénio','Bromo','Crípton','Rubídeo','Estrôncio','Ítrio','Zircónio','Nióbio','Molibdénio','Tecnécio','Rutério','Ródio','Paládio','Prata','Cádmio','Índio','Estanho','Antimónio','Telúrio','Iodo','Xénon','Césio','Bário','Lantânio','Cério','Praseodímio','Neodímio','Promécio','Samário','Európio','Gadolínio','Térbio','Disprósio','Hólmio','Érbio','Túlio','Itérbio','Lutécio','Háfnio','Tântalo','Tungsténio','Rénio','Ósmio','Irídio','Platina','Ouro','Mercúrio','Tálio','Chumbo','Bismuto','Polónio','Ástato','Rádon','Frâncio','Rádio','Actínio','Tório','Protactínio','Urânio','Neptúnio','Plutónio','Amerício','Cúrio','Berkélio','Califórnio','Einsténio','Férmio','Mendelévio','Nobélio','Lawrêncio','Rutherfórdio','Dúbnio','Seabórgio','Bóhrio','Hássio','Meitnério','Darmstácio','Roentgénio','Copernício','Nipónio','Fleróvio','Moscóvio','Livermório','Tenesso','Oganésson']

def ftp(number):
    symbol = 'H'
    name = 'Hidrogénio'
    mar = 1.01
    dist = "1"
    g = 1
    p = 1
    if number == 1:
        symbol = 'H'
        name = 'Hidrogénio'
        number = 1
        mar = 1.01
        dist = "1"
        g = 1
        p = 1
    elif number == 2:
        symbol = 'He'
        name = 'Hélio'
        number = 2
        mar = 4.01
        dist = "2"
        g = 1
        p = 18
    elif number == 3:
        symbol = 'Li'
        name = 'Lítio'
        number = 3
        mar = 6.94
        dist = "2, 1"
        g = 1
        p = 2
    elif number == 4:
        symbol = 'Be'
        name = 'Berílio'
        number = 4
        mar = 9.01
        dist = "2, 2"
        g = 2
        p = 2
    elif number == 5:
        symbol = 'B'
        name = 'Boro'
        number = 5
        mar = 10.81
        dist = "2, 3"
        g = 13
        p = 2
    elif number == 6:
        symbol = 'C'
        name = 'Carbono'
        number = 6
        mar = 12.01
        dist = "2, 4"
        g = 14
        p = 2
    elif number == 7:
        symbol = 'N'
        name = 'Nitrogénio'
        number = 7
        mar = 14.01
        dist = "2, 5"
        g = 15
        p = 2
    elif number == 8:
        symbol = 'O'
        name = 'Oxigénio'
        number = 8
        mar = 16.00
        dist = "2, 6"
        g = 16
        p = 2
    elif number == 9:
        symbol = 'F'
        name = 'Flúor'
        number = 9
        mar = 19.00
        dist = "2, 7"
        g = 17
        p = 2
    elif number == 10:
        symbol = 'Ne'
        name = 'Néon'
        number = 10
        mar = 20.18
        dist = "2, 8"
        g = 18
        p = 2
    elif number == 11:
        symbol = 'Na'
        name = 'Sódio'
        number = 11
        mar = 22.99
        dist = "2, 8, 1"
        g = 1
        p = 3
    elif number == 12:
        symbol = 'Mg'
        name = 'Magnésio'
        number = 12
        mar = 24.31
        dist = "2, 8, 2"
        g = 2
        p = 3
    elif number == 13:
        symbol = 'Al'
        name = 'Alumínio'
        number = 13
        mar = 26.98
        dist = "2, 8, 3"
        g = 13
        p = 3
    elif number == 14:
        symbol = 'Si'
        name = 'Silício'
        number = 14
        mar = 28.09
        dist = "2, 8, 4"
        g = 14
        p = 3
    elif number == 15:
        symbol = 'P'
        name = 'Fósforo'
        number = 15
        mar = 30.97
        dist = "2, 8, 5"
        g = 15
        p = 3
    elif number == 16:
        symbol = 'S'
        name = 'Enxofre'
        number = 16
        mar = 32.06
        dist = "2, 8, 6"
        g = 16
        p = 3
    elif number == 17:
        symbol = 'Cl'
        name = 'Cloro'
        number = 17
        mar = 35.45
        dist = "2, 8, 7"
        g = 17
        p = 3
    elif number == 18:
        symbol = 'Ar'
        name = 'Árgon'
        number = 18
        mar = 39.95
        dist = "2, 8, 8"
        g = 18
        p = 3
    elif number == 19:
        symbol = 'K'
        name = 'Potássio'
        number = 19
        mar = 39.10
        dist = "2, 8, 8, 1"
        g = 1
        p = 4
    elif number == 20:
        symbol = 'Ca'
        name = 'Cálcio'
        number = 20
        mar = 40.08
        dist = "2, 8, 8, 2"
        g = 2
        p = 4
    elif number == 21:
        symbol = 'Sc'
        name = 'Escândio'
        number = 21
        mar = 44.96
        dist = "2, 8, 9, 2"
        g = 3
        p = 4
    elif number == 22:
        symbol = 'Ti'
        name = 'Titânio'
        number = 22
        mar = 47.87
        dist ="2, 8, 10, 2"
        g = 4
        p = 4
    elif number == 23:
        symbol = 'V'
        name = 'Vanádio'
        number = 23
        mar = 50.94
        dist ="2, 8, 11, 2"
        g = 5
        p = 4
    elif number == 24:
        symbol = 'Cr'
        name = 'Crómo'
        number = 24
        mar = 52.02
        dist ="2, 8, 13, 1"
        g = 6
        p = 4
    elif number == 25:
        symbol = 'Mn'
        name = 'Manganês'
        number = 25
        mar = 54.94
        dist ="2, 8, 13, 2"
        g = 7
        p = 4
    elif number == 26:
        symbol = 'Fe'
        name = 'Ferro'
        number = 26
        mar = 55.85
        dist ="2, 8, 14, 2"
        g = 8
        p = 4
    elif number == 27:
        symbol = 'Co'
        name = 'Cobalto'
        number = 27
        mar = 58.93
        dist ="2, 8, 15, 2"
        g = 9
        p = 4
    elif number == 28:
        symbol = 'Ni'
        name = 'Níquel'
        number = 28
        mar = 58.69
        dist ="2, 8, 16, 2"
        g = 10
        p = 4
    elif number == 29:
        symbol = 'Cu'
        name = 'Cobre'
        number = 29
        mar = 63.55
        dist ="2, 8, 18, 1"
        g = 11
        p = 4
    elif number == 30:
        symbol = 'Zn'
        name = 'Zinco'
        number = 30
        mar = 65.38
        dist ="2, 8, 18, 1"
        g = 12
        p = 4
    elif number == 31:
        symbol = 'Ga'
        name = 'Gálio'
        number = 31
        mar = 69.72
        dist ="2, 8, 18, 3"
        g = 13
        p = 4
    elif number == 32:
        symbol = 'Ge'
        name = 'Germânio'
        number = 32
        mar = 72.63
        dist ="2, 8, 18, 4"
        g = 14
        p = 4
    elif number == 33:
        symbol = 'As'
        name = 'Arsénio'
        number = 33
        mar = 74.92
        dist ="2, 8, 18, 5"
        g = 15
        p = 4
    elif number == 34:
        symbol = 'Se'
        name = 'Selénio'
        number = 34
        mar = 78.97
        dist ="2, 8, 18, 6"
        g = 16
        p = 4
    elif number == 35:
        symbol = 'Br'
        name = 'Bromo'
        number = 35
        mar = 79.90
        dist ="2, 8, 18, 7"
        g = 17
        p = 4
    elif number == 36:
        symbol = 'Kr'
        name = 'Crípton'
        number = 36
        mar = 83.80
        dist ="2, 8, 18, 8"
        g = 18
        p = 4
    elif number == 37:
        symbol = 'Rb'
        name = 'Rubídeo'
        number = 37
        mar = 85.47
        dist ="2, 8, 18, 8, 1"
        g = 1
        p = 5
    elif number == 38:
        symbol = 'Sr'
        name = 'Estrôncio'
        number = 38
        mar = 87.62
        dist ="2, 8, 18, 8, 2"
        g = 2
        p = 5
    elif number == 39:
        symbol = 'Y'
        name = 'Ítrio'
        number = 39
        mar = 88.91
        dist ="2, 8, 18, 9, 2"
        g = 3
        p = 5
    elif number == 40:
        symbol = 'Zr'
        name = 'Zircónio'
        number = 40
        mar = 91.22
        dist ="2, 8, 18, 10, 2"
        g = 4
        p = 5
    elif number == 41:
        symbol = 'Nb'
        name = 'Nióbio'
        number = 41
        mar = 92.91
        dist ="2, 8, 18, 12, 1"
        g = 5
        p = 5
    elif number == 42:
        symbol = 'Mo'
        name = 'Molibdénio'
        number = 42
        mar = 95.95
        dist ="2, 8, 18, 13, 1"
        g = 6
        p = 5
    elif number == 43:
        symbol = 'Tc'
        name = 'Tecnécio'
        number = 43
        mar = 98
        dist ="2, 8, 18, 13, 2"
        g = 7
        p = 5
    elif number == 44:
        symbol = 'Ru'
        name = 'Rutério'
        number = 44
        mar = 101.07
        dist ="2, 8, 18, 15, 1"
        g = 8
        p = 18
    elif number == 45:
        symbol = 'Rh'
        name = 'Ródio'
        number = 45
        mar = 102.91
        dist ="2, 8, 18, 16, 1"
        g = 9
        p = 5
    elif number == 46:
        symbol = 'Pd'
        name = 'Paládio'
        number = 46
        mar = 106.42
        dist ="2, 8, 18, 18"
        g = 10
        p = 5
    elif number == 47:
        symbol = 'Ag'
        name = 'Prata'
        number = 47
        mar = 107.87
        dist ="2, 8, 18, 18, 1"
        g = 11
        p = 5
    elif number == 48:
        symbol = 'Cd'
        name = 'Cádmio'
        number = 48
        mar = 112.41
        dist ="2, 8, 18, 18, 2"
        g = 12
        p = 5
    elif number == 49:
        symbol = 'In'
        name = 'Índio'
        number = 49
        mar = 114.82
        dist ="2, 8, 18, 18, 3"
        g = 13
        p = 5
    elif number == 50:
        symbol = 'Sn'
        name = 'Estanho'
        number = 50
        mar = 118.71
        dist ="2, 8, 18, 18, 4"
        g = 14
        p = 5
    elif number == 51:
        symbol = 'Sb'
        name = 'Antimónio'
        number = 51
        mar = 121.76
        dist ="2, 8, 18, 18, 5"
        g = 15
        p = 5
    elif number == 52:
        symbol = 'Te'
        name = 'Telúrio'
        number = 52
        mar = 127.60
        dist ="2, 8, 18, 18, 6"
        g = 16
        p = 5
    elif number == 53:
        symbol = 'I'
        name = 'Iodo'
        number = 53
        mar = 126.90
        dist ="2, 8, 18, 18, 7"
        g = 17
        p = 5
    elif number == 54:
        symbol = 'Xe'
        name = 'Xénon'
        number = 54
        mar = 131.29
        dist ="2, 8, 18, 18, 8"
        g = 18
        p = 5
    elif number == 55:
        symbol = 'Cs'
        name = 'Césio'
        number = 55
        mar = 132.91
        dist ="2, 8, 18, 18, 8, 1"
        g = 1
        p = 6
    elif number == 56:
        symbol = 'Ba'
        name = 'Bário'
        number = 56
        mar = 137.33
        dist ="2, 8, 18, 18, 8, 2"
        g = 2
        p = 6
    elif number == 57:
        symbol = 'La'
        name = 'Lantânio'
        number = 57
        mar = 138.91
        dist ="2, 8, 18, 18, 9, 2"
        g = 3
        p = 6
    elif number == 58:
        symbol = 'Ce'
        name = 'Cério'
        number = 58
        mar = 140.12
        dist ="2, 8, 18, 19, 9, 2"
        g = 3
        p = 6
    elif number == 59:
        symbol = 'Pr'
        name = 'Praseodímio'
        number = 59
        mar = 140.91
        dist ="2, 8, 18, 21, 8, 2"
        g = 3
        p = 6
    elif number == 60:
        symbol = 'Nd'
        name = 'Neodímio'
        number = 60
        mar = 144.24
        dist ="2, 8, 18, 22, 8, 2"
        g = 3
        p = 6
    elif number == 61:
        symbol = 'Pm'
        name = 'Promécio'
        number = 61
        mar = 145
        dist ="2, 8, 18, 23, 8, 2"
        g = 3
        p = 6
    elif number == 62:
        symbol = 'Sm'
        name = 'Samário'
        number = 62
        mar = 150.36
        dist ="2, 8, 18, 24, 8, 2"
        g = 3
        p = 6
    elif number == 63:
        symbol = 'Eu'
        name = 'Európio'
        number = 63
        mar = 151.96
        dist ="2, 8, 18, 25, 8, 2"
        g = 3
        p = 6
    elif number == 64:
        symbol = 'Gd'
        name = 'Gadolínio'
        number = 64
        mar = 157.25
        dist ="2, 8, 18, 25, 9, 2"
        g = 3
        p = 6
    elif number == 65:
        symbol = 'Tb'
        name = 'Térbio'
        number = 65
        mar = 158.93
        dist ="2, 8, 18, 27, 8, 2"
        g = 3
        p = 6
    elif number == 66:
        symbol = 'Dy'
        name = 'Disprósio'
        number = 66
        mar = 162.50
        dist ="2, 8, 18, 28, 8, 2"
        g = 3
        p = 6
    elif number == 67:
        symbol = 'Ho'
        name = 'Hólmio'
        number = 67
        mar = 164.93
        dist ="2, 8, 18, 29, 8, 2"
        g = 3
        p = 6
    elif number == 68:
        symbol = 'Er'
        name = 'Érbio'
        number = 68
        mar = 167.26
        dist ="2, 8, 18, 30, 8, 2"
        g = 3
        p = 6
    elif number == 69:
        symbol = 'Tm'
        name = 'Túlio'
        number = 69
        mar = 168.93
        dist ="2, 8, 18, 31, 8, 2"
        g = 3
        p = 6
    elif number == 70:
        symbol = 'Yb'
        name = 'Itérbio'
        number = 70
        mar = 173.05
        dist ="2, 8, 18, 32, 8, 2"
        g = 3
        p = 6
    elif number == 71:
        symbol = 'Lu'
        name = 'Lutécio'
        number = 71
        mar = 174.97
        dist ="2, 8, 18, 32, 9, 2"
        g = 3
        p = 6
    elif number == 72:
        symbol = 'Hf'
        name = 'Háfnio'
        number = 72
        mar = 178.49
        dist ="2, 8, 18, 32, 10, 2"
        g = 4
        p = 6
    elif number == 73:
        symbol = 'Ta'
        name = 'Tântalo'
        number = 73
        mar = 180.95
        dist ="2, 8, 18, 32, 11, 2"
        g = 5
        p = 6
    elif number == 74:
        symbol = 'W'
        name = 'Tungsténio'
        number = 74
        mar = 183.84
        dist ="2, 8, 18, 32, 12, 2"
        g = 6
        p = 6
    elif number == 75:
        symbol = 'Re'
        name = 'Rénio'
        number = 75
        mar = 186.21
        dist ="2, 8, 18, 32, 13, 2"
        g = 7
        p = 6
    elif number == 76:
        symbol = 'Os'
        name = 'Ósmio'
        number = 76
        mar = 190.23
        dist ="2, 8, 18, 32, 14, 2"
        g = 8
        p = 6
    elif number == 77:
        symbol = 'Ir'
        name = 'Irídio'
        number = 77
        mar = 192.22
        dist ="2, 8, 18, 32, 15, 2"
        g = 9
        p = 6
    elif number == 78:
        symbol = 'Pt'
        name = 'Platina'
        number = 78
        mar = 195.08
        dist ="2, 8, 18, 32, 17, 1"
        g = 10
        p = 6
    elif number == 79:
        symbol = 'Au'
        name = 'Ouro'
        number = 79
        mar = 196.97
        dist ="2, 8, 18, 32, 18, 1"
        g = 11
        p = 6
    elif number == 80:
        symbol = 'Hg'
        name = 'Mercúrio'
        number = 80
        mar = 200.59
        dist ="2, 8, 18, 32, 18, 2"
        g = 12
        p = 6
    elif number == 81:
        symbol = 'Tl'
        name = 'Tálio'
        number = 81
        mar = 204.38
        dist ="2, 8, 18, 32, 18, 3"
        g = 13
        p = 6
    elif number == 82:
        symbol = 'Pb'
        name = 'Chumbo'
        number = 82
        mar = 207.20
        dist ="2, 8, 18, 32, 18, 4"
        g = 14
        p = 6
    elif number == 83:
        symbol = 'Bi'
        name = 'Bismuto'
        number = 83
        mar = 208.98
        dist ="2, 8, 18, 32, 18, 5"
        g = 15
        p = 6
    elif number == 84:
        symbol = 'Po'
        name = 'Polónio'
        number = 84
        mar = 209
        dist ="2, 8, 18, 32, 18, 6"
        g = 16
        p = 6
    elif number == 85:
        symbol = 'At'
        name = 'Ástato'
        number = 85
        mar = 210
        g = 17
        dist ="2, 8, 18, 32, 18, 7"
        p = 6
    elif number == 86:
        symbol = 'Rn'
        name = 'Rádon'
        number = 86
        mar = 222
        g = 18
        p = 6
        dist ="2, 8, 18, 32, 18, 8"
    elif number == 87:
        symbol = 'Fr'
        name = 'Frâncio'
        number = 87
        mar = 223
        dist = "2, 8, 18, 32, 18, 8, 1"
        g = 1
        p = 7
    elif number == 88:
        dist ="2, 8, 18, 32, 18, 8, 2"
        symbol = 'Ra'
        name = 'Rádio'
        number = 88
        mar = 226
        g = 2
        p = 7
    elif number == 89:
        symbol = 'Ac'
        dist ="2, 8, 18, 32, 18, 9, 2"
        name = 'Actínio'
        number = 89
        mar = 227
        g = 3
        p = 7
    elif number == 90:
        symbol = 'Th'
        name = 'Tório'
        dist ="2, 8, 18, 32, 18, 10, 2"
        number = 90
        mar = 232.04
        g = 3
        p = 7
    elif number == 91:
        symbol = 'Pa'
        name = 'Protactínio'
        number = 91
        dist ="2, 8, 18, 32, 20, 9, 2"
        mar = 231.04
        g = 3
        p = 7
    elif number == 92:
        symbol = 'U'
        name = 'Urânio'
        number = 92
        mar = 238.03
        dist ="2, 8, 18, 32, 21, 9, 2"
        g = 3
        p = 7
    elif number == 93:
        symbol = 'Np'
        name = 'Neptúnio'
        number = 93
        mar = 237
        g = 3
        dist ="2, 8, 18, 32, 22, 9, 2"
        p = 7
    elif number == 94:
        symbol = 'Pu'
        name = 'Plutónio'
        number = 94
        mar = 244
        g = 3
        p = 7
        dist ="2, 8, 18, 32, 24, 8, 2"
    elif number == 95:
        symbol = 'Am'
        name = 'Amerício'
        number = 95
        mar = 243
        g = 3
        p = 7
        dist = "2, 8, 18, 32, 25, 8, 2"
    elif number == 96:
        dist ="2, 8, 18, 32, 25, 9, 2"
        symbol = 'Cm'
        name = 'Cúrio'
        number = 96
        mar = 247
        g = 3
        p = 7
    elif number == 97:
        symbol = 'Bk'
        dist ="2, 8, 18, 32, 27, 8, 2"
        name = 'Berkélio'
        number = 97
        mar = 247
        g = 3
        p = 7
    elif number == 98:
        symbol = 'Cf'
        name = 'Califórnio'
        dist ="2, 8, 18, 32, 28, 8, 2"
        number = 98
        mar = 252
        g = 3
        p = 7
    elif number == 99:
        symbol = 'Es'
        name = 'Einsténio'
        number = 99
        dist ="2, 8, 18, 32, 29, 8, 2"
        mar = 252
        g = 3
        p = 7
    elif number == 100:
        symbol = 'Fm'
        name = 'Férmio'
        number = 100
        mar = 257
        dist ="2, 8, 18, 32, 30, 8, 2"
        g = 3
        p = 7
    elif number == 101:
        symbol = 'Md'
        name = 'Mendelévio'
        number = 101
        mar = 258
        dist ="2, 8, 18, 32, 31, 8, 2"
        g = 3
        p = 7
    elif number == 102:
        symbol = 'No'
        name = 'Nobélio'
        number = 102
        mar = 259
        dist ="2, 8, 18, 32, 32, 8, 2"
        g = 3
        p = 7
    elif number == 103:
        symbol = 'Lr'
        name = 'Lawrêncio'
        number = 103
        mar = 262
        dist ="2, 8, 18, 32, 32, 8, 3"
        g = 3
        p = 7
    elif number == 104:
        symbol = 'Rf'
        name = 'Rutherfórdio'
        number = 104
        mar = 261
        dist ="2, 8, 18, 32, 32, 10, 2"
        g = 4
        p = 7
    elif number == 105:
        symbol = 'Db'
        name = 'Dúbnio'
        number = 105
        mar = 262
        dist ="2, 8, 18, 32, 32, 11, 2"
        g = 5
        p = 7
    elif number == 106:
        symbol = 'Sg'
        name = 'Seabórgio'
        number = 106
        mar = 266
        dist ="2, 8, 18, 32, 32, 12, 2"
        g = 6
        p = 7
    elif number == 107:
        symbol = 'Bh'
        name = 'Bóhrio'
        number = 107
        mar = 264
        dist ="2, 8, 18, 32, 32, 13, 2"
        g = 7
        p = 7
    elif number == 108:
        symbol = 'Hs'
        name = 'Hássio'
        number = 108
        mar = 277
        dist ="2, 8, 18, 32, 32, 14, 2"
        g = 8
        p = 7
    elif number == 109:
        symbol = 'Mt'
        name = 'Meitnério'
        number = 109
        mar = 268
        dist ="2, 8, 18, 32, 32, 15, 2"
        g = 9
        p = 7
    elif number == 110:
        symbol = 'Ds'
        name = 'Darmstácio'
        number = 110
        mar = 281
        dist ="2, 8, 18, 32, 32, 17, 1"
        g = 10
        p = 7
    elif number == 111:
        symbol = 'Rg'
        name = 'Roentgénio'
        number = 111
        mar = 280
        dist ="2, 8, 18, 32, 32, 17, 2"
        g = 11
        p = 7
    elif number == 112:
        symbol = 'Cn'
        name = 'Copernício'
        number = 112
        mar = 285
        dist ="2, 8, 18, 32, 32, 18, 2"
        g = 12
        p = 7
    elif number == 113:
        symbol = 'Nh'
        name = 'Nipónio'
        number = 113
        mar = 286
        dist ="2, 8, 18, 32, 32, 18, 3"
        g = 13
        p = 7
    elif number == 114:
        symbol = 'Fl'
        name = 'Fleróvio'
        number = 114
        mar = 289
        dist ="2, 8, 18, 32, 32, 18, 4"
        g = 14
        p = 7
    elif number == 115:
        symbol = 'Mc'
        name = 'Moscóvio'
        number = 115
        mar = 289
        dist ="2, 8, 18, 32, 32, 18, 5"
        g = 15
        p = 7
    elif number == 116:
        symbol = 'Lv'
        name = 'Livermório'
        number = 116
        mar = 293
        dist ="2, 8, 18, 32, 32, 18, 6"
        g = 16
        p = 7
    elif number == 117:
        symbol = 'Ts'
        name = 'Tenesso'
        number = 117
        mar = 294
        dist ="2, 8, 18, 32, 32, 18, 7"
        g = 17
        p = 7
    elif number == 118:
        symbol = 'Og'
        name = 'Oganésson'
        number = 118
        mar = 294
        dist ="2, 8, 18, 32, 32, 18, 8"
        g = 18
        p = 7
    else:
        symbol = symbol
        name = name
        number = number
        mar = mar
        dist = dist
        g = g
        p = p
    return [symbol, name, number, mar, dist, g, p]


def tp():
    search = st.text_input("Procura")
    if search == "":
        number = st.slider("", 1, 118, step=1)
        info = ftp(int(number))
        st.title(f"{info[0]} - {info[1]}")
        st.header(f"Número Atómico: {info[2]}")
        st.header(f"Massa Atómica relativa: {info[3]}")
        st.header(f"Distribuição Eletrónica: {info[4]}")
        st.header(f"Grupo: {info[5]}")
        st.header(f"Período: {info[6]}")
    else:
        indices = []
        for i, elem in enumerate(elements):
            if search.lower() in elem.lower():
                indices.append(i)
        if indices == []:
            st.header("Desculpa! Não encontramos nada.") 
        else:
            for j in indices:
                info = ftp(j+1)
                ex = st.beta_expander(f"{info[0]} - {info[1]}")
                ex.header(f"Número Atómico: {info[2]}")
                ex.header(f"Massa Atómica relativa: {info[3]}")
                ex.header(f"Distribuição Eletrónica: {info[4]}")
                ex.header(f"Grupo: {info[5]}")
                ex.header(f"Período: {info[6]}")




