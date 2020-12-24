area = ["mm²", "cm²", "dm²", "m²", "Km²"]
dist = ["nm", "µm", "mm", "cm", "dm", "m", "Km"]
ene = ["J", "KJ", "MJ", "GJ", "Wh", "KWh", "MWh", "GWh"]
mass = ["mg", "g", "kg", "ton"]
pot = ["W", "KW", "MW", "GW"]
temp = ["ºC", "ºK", "ºT"]
time = ["ns", "µs", "ms", "s", "min", "hora"]
vel = ["mm/s", "cm/s", "dm/s", "m/s", "Km/s", "m/h", "Km/h"]
vol = ["mm³", "cm³", "dm³", "m³", "mL", "cL", "dL", "L"]
def units(con):
    if con == "Área":
        unit = area
    elif con == "Distância":
        unit = dist
    elif con == "Energia":
        unit = ene
    elif con == "Massa":
        unit = mass
    elif con == "Potência":
        unit = pot
    elif con == "Temperatura":
        unit = temp
    elif con == "Tempo":
        unit = time
    elif con == "Velocidade":
        unit = vel
    elif con == "Volume":
        unit = vol
    return unit


def farea(v, u1, u2):
    if u1 == u2:
        return v
    elif u1 == "mm²":
        if u2 == "cm²":
            return v / 100
        elif u2 == "dm²":
            return v / 10000
        elif u2 == "m²":
            return v / 1000000
        elif u2 == "Km²":
            return v / 1e12
    elif u1 == "cm²":
        if u2 == "mm²":
            return v * 100
        elif u2 == "dm²":
            return v / 100
        elif u2 == "m²":
            return v / 10000
        elif u2 == "Km²":
            return v / 1e10
    elif u1 == "dm²":
        if u2 == "mm²":
            return v * 10000
        elif u2 == "cm²":
            return v * 100
        elif u2 == "m²":
            return v / 100
        elif u2 == "Km²":
            return v / 1e8
    elif u1 == "m²":
        if u2 == "mm²":
            return v * 1000000
        elif u2 == "cm²":
            return v * 10000
        elif u2 == "dm²":
            return v * 100
        elif u2 == "Km²":
            return v / 1e6
    elif u1 == "Km²":
        if u2 == "mm²":
            return v * 1e12
        elif u2 == "cm²":
            return v * 1e10
        elif u2 == "dm²":
            return v * 1e8
        elif u2 == "m²":
            return v * 1e6

def fdist(v, u1, u2):
    if u1 == u2:
        return v
    elif u1 == "nm":
        if u2 == "µm":
            return v / 1000
        elif u2 == "mm":
            return v / 1000000
        elif u2 == "cm":
            return v / 10000000
        elif u2 == "dm":
            return v / 100000000
        elif u2 == "m":
            return v / 1000000000
        elif u2 == "Km":
            return v / 1000000000000
    elif u1 == "µm":
        if u2 == "nm":
            return v * 1000
        elif u2 == "mm":
            return v / 1000
        elif u2 == "cm":
            return v / 10000
        elif u2 == "dm":
            return v / 100000
        elif u2 == "m":
            return v / 1000000
        elif u2 == "Km":
            return v / 1000000000
    elif u1 == "mm":
        if u2 == "nm":
            return v * 1000000
        elif u2 == "µm":
            return v * 1000
        elif u2 == "cm":
            return v / 10
        elif u2 == "dm":
            return v / 100
        elif u2 == "m":
            return v / 1000
        elif u2 == "Km":
            return v / 1000000
    elif u1 == "cm":
        if u2 == "nm":
            return v * 10000000
        elif u2 == "µm":
            return v * 10000
        elif u2 == "mm":
            return v * 10
        elif u2 == "dm":
            return v / 10
        elif u2 == "m":
            return v / 100
        elif u2 == "Km":
            return v / 100000
    elif u1 == "dm":
        if u2 == "nm":
            return v * 100000000
        elif u2 == "µm":
            return v * 100000
        elif u2 == "mm":
            return v * 100
        elif u2 == "cm":
            return v * 10
        elif u2 == "m":
            return v / 10
        elif u2 == "Km":
            return v / 10000
    elif u1 == "m":
        if u2 == "nm":
            return v * 1000000000
        elif u2 == "µm":
            return v * 1000000
        elif u2 == "mm":
            return v * 1000
        elif u2 == "cm":
            return v * 100
        elif u2 == "dm":
            return v * 10
        elif u2 == "Km":
            return v / 1000
    elif u1 == "Km":
        if u2 == "nm":
            return v * 1000000000000
        elif u2 == "µm":
            return v * 1000000000
        elif u2 == "mm":
            return v * 1000000
        elif u2 == "cm":
            return v * 100000
        elif u2 == "dm":
            return v * 10000
        elif u2 == "m":
            return v * 1000
    

def fene(v, u1, u2):
    if u1 == u2:
        return v
    elif u1 == "J":
        if u2 == "KJ":
            return v / 1000
        elif u2 == "MJ":
            return v / 1000000
        elif u2 == "GJ":
            return v / 1000000000
        elif u2 == "Wh":
            return v / 3600
        elif u2 == "KWh":
            return v / 3600000
        elif u2 == "MWh":
            return v / 3600000000
        elif u2 == "GWh":
            return v / 3600000000000
    elif u1 == "KJ":
        if u2 == "J":
            return v * 1000
        elif u2 == "MJ":
            return v / 1000
        elif u2 == "GJ":
            return v / 1000000
        elif u2 == "Wh":
            return v / 3600 * 1000
        elif u2 == "KWh":
            return v / 3600
        elif u2 == "MWh":
            return v / 3600000
        elif u2 == "GWh":
            return v / 3600000000
    elif u1 == "MJ":
        if u2 == "J":
            return v * 1000000
        elif u2 == "KJ":
            return v * 1000
        elif u2 == "GJ":
            return v / 1000
        elif u2 == "Wh":
            return v / 3600 * 1000000
        elif u2 == "KWh":
            return v / 3600 * 1000
        elif u2 == "MWh":
            return v / 3600
        elif u2 == "GWh":
            return v / 3600000
    elif u1 == "GJ":
        if u2 == "J":
            return v * 1000000000
        elif u2 == "KJ":
            return v * 1000000
        elif u2 == "MJ":
            return v * 1000
        elif u2 == "Wh":
            return v / 3600 * 1000000000
        elif u2 == "KWh":
            return v / 3600 * 1000000
        elif u2 == "MWh":
            return v / 3600 * 1000
        elif u2 == "GWh":
            return v / 3600
    elif u1 == "Wh":
        if u2 == "J":
            return v * 3600
        elif u2 == "KJ":
            return v * 3.6
        elif u2 == "MJ":
            return v * 0.0036
        elif u2 == "GJ":
            return v * 0.0000036
        elif u2 == "KWh":
            return v / 1000
        elif u2 == "MWh":
            return v / 1000000
        elif u2 == "GWh":
            return v / 1000000000
    elif u1 == "KWh":
        if u2 == "J":
            return v * 3600000
        elif u2 == "KJ":
            return v * 3600
        elif u2 == "MJ":
            return v * 3.6
        elif u2 == "GJ":
            return v * 0.0036
        elif u2 == "Wh":
            return v * 1000
        elif u2 == "MWh":
            return v / 1000
        elif u2 == "GWh":
            return v / 1000000
    elif u1 == "MWh":
        if u2 == "J":
            return v * 3600000000
        elif u2 == "KJ":
            return v * 3600000
        elif u2 == "MJ":
            return v * 3600
        elif u2 == "GJ":
            return v * 3.6
        elif u2 == "Wh":
            return v * 1000000
        elif u2 == "KWh":
            return v * 1000
        elif u2 == "GWh":
            return v / 1000
    elif u1 == "GWh":
        if u2 == "J":
            return v * 3600000000000
        elif u2 == "KJ":
            return v * 3600000000
        elif u2 == "MJ":
            return v * 3600000
        elif u2 == "GJ":
            return v * 3600
        elif u2 == "Wh":
            return v * 1000000000
        elif u2 == "KWh":
            return v * 1000000
        elif u2 == "MWh":
            return v * 1000

def fmass(v, u1, u2):
    if u1 == u2:
        return v
    elif u1 == "mg":
        if u2 == "g":
            return v / 1000
        elif u2 == "Kg":
            return v / 1000000
        elif u2 == "ton":
            return v / 1000000000
    elif u1 == "g":
        if u2 == "mg":
            return v * 1000
        elif u2 == "Kg":
            return v / 1000
        elif u2 == "ton":
            return v / 1000000
    elif u1 == "Kg":
        if u2 == "mg":
            return v * 1000000
        elif u2 == "g":
            return v * 1000
        elif u2 == "ton":
            return v / 1000
    elif u1 == "ton":
        if u2 == "mg":
            return v * 1000000000
        elif u2 == "g":
            return v * 1000000
        elif u2 == "Kg":
            return v * 1000

def fpot(v, u1, u2):
    if u1 == u2:
        return v
    elif u1 == "W":
        if u2 == "KW":
            return v / 1000
        elif u2 == "MW":
            return v / 1000000
        elif u2 == "GW":
            return v / 1000000000
    elif u1 == "KW":
        if u2 == "W":
            return v * 1000
        elif u2 == "MW":
            return v / 1000
        elif u2 == "GW":
            return v / 1000000
    elif u1 == "MW":
        if u2 == "W":
            return v * 1000000
        elif u2 == "KW":
            return v * 1000
        elif u2 == "GW":
            return v / 1000
    elif u1 == "GW":
        if u2 == "W":
            return v * 1000000000
        elif u2 == "KW":
            return v * 1000000
        elif u2 == "GW":
            return v * 1000

def ftemp(v, u1, u2):
    if u1 == u2:
        return v
    elif u1 == "ºC":
        if u2 == "ºF":
            return v * 1.8 + 32 
        elif u2 == "ºK":
            return v + 273.15
    elif u1 == "ºF":
        if u2 == "ºC":
            return (v - 32) / 1.8
        elif u2 == "ºK":
            return (v - 32) / 1.8 + 273.15
    elif u1 == "ºK":
        if u2 == "ºC":
            return v - 273.15
        elif u2 == "ºF":
            return (v - 273.15 - 32) / 1.8 

def ftime(v, u1, u2):
    if u1 == u2:
        return v
    elif u1 == "ns":
        if u2 == "µs":
            return v * 0.001
        elif u2 == "ms":
            return v * 1e-6
        elif u2 == "s":
            return v * 1e-9
        elif u2 == "min":
            return v * 1e-9 / 60
        elif u2 == "hora":
            return v * 1e-9 / 60 / 60
    elif u1 == "µs":
        if u2 == "ns":
            return v * 1000
        elif u2 == "ms":
            return v / 1000
        elif u2 == "s":
            return v / 1000000
        elif u2 == "min":
            return v / 1000000 / 60
        elif u2 == "hora":
            return v / 1000000 / 60 / 60
    elif u1 == "ms":
        if u2 == "ns":
            return v * 1000000
        elif u2 == "µs":
            return v * 1000
        elif u2 == "s":
            return v / 1000
        elif u2 == "min":
            return v / 1000 / 60
        elif u2 == "hora":
            return v / 1000 / 60 / 60
    elif u1 == "s":
        if u2 == "ns":
            return v * 1000000000
        elif u2 == "µs":
            return v * 1000000
        elif u2 == "ms":
            return v * 1000
        elif u2 == "min":
            return v / 60
        elif u2 == "hora":
            return v / 60 / 60
    elif u1 == "min":
        if u2 == "ns":
            return v * 1000000000 * 60
        elif u2 == "µs":
            return v * 1000000 * 60
        elif u2 == "ms":
            return v * 1000 * 60
        elif u2 == "s":
            return v * 60
        elif u2 == "hora":
            return v / 60
    elif u1 == "hora":
        if u2 == "ns":
            return v * 1000000000 * 60 * 60
        elif u2 == "µs":
            return v * 1000000 * 60 * 60
        elif u2 == "ms":
            return v * 1000 * 60 * 60
        elif u2 == "s":
            return v * 60 * 60
        elif u2 == "min":
            return v * 60

def fvel(v, u1, u2):
    if u1 == u2:
        return v
    elif u1 == "mm/s":
        if u2 == "cm/s":
            return v / 10
        elif u2 == "dm/s":
            return v / 100
        elif u2 == "m/s":
            return v / 1000
        elif u2 == "Km/s":
            return v / 1000000
        elif u2 == "m/h":
            return v * 3.6
        elif u2 == "Km/h":
            return v * 3.6 / 1000
    elif u1 == "cm/s":
        if u2 == "mm/s":
            return v * 10
        elif u2 == "dm/s":
            return v / 10
        elif u2 == "m/s":
            return v / 100
        elif u2 == "Km/s":
            return v / 100000
        elif u2 == "m/h":
            return v * 36
        elif u2 == "Km/h":
            return v * 36 / 1000
    elif u1 == "dm/s":
        if u2 == "mm/s":
            return v * 100
        elif u2 == "cm/s":
            return v * 10
        elif u2 == "m/s":
            return v / 10
        elif u2 == "Km/s":
            return v / 10000
        elif u2 == "m/h":
            return v * 360
        elif u2 == "Km/h":
            return v * 360 / 1000
    elif u1 == "m/s":
        if u2 == "mm/s":
            return v * 1000
        elif u2 == "cm/s":
            return v * 100
        elif u2 == "dm/s":
            return v * 100
        elif u2 == "Km/s":
            return v / 1000
        elif u2 == "m/h":
            return v * 3600
        elif u2 == "Km/h":
            return v * 3600 / 1000
    elif u1 == "Km/s":
        if u2 == "mm/s":
            return v * 1000000
        elif u2 == "cm/s":
            return v * 100000
        elif u2 == "dm/s":
            return v * 100000
        elif u2 == "m/s":
            return v * 1000
        elif u2 == "m/h":
            return v * 3600000
        elif u2 == "Km/h":
            return v * 3600
    elif u1 == "m/h":
        if u2 == "mm/s":
            return v / 3.6
        elif u2 == "cm/s":
            return v / 36
        elif u2 == "dm/s":
            return v / 360
        elif u2 == "m/s":
            return v / 3600
        elif u2 == "Km/s":
            return v / 3600000
        elif u2 == "Km/h":
            return v / 1000
    elif u1 == "Km/h":
        if u2 == "mm/s":
            return v / 3.6 * 1000
        elif u2 == "cm/s":
            return v / 36 * 1000
        elif u2 == "dm/s":
            return v / 360 * 1000
        elif u2 == "m/s":
            return v / 3600 * 1000
        elif u2 == "Km/s":
            return v / 3600000 * 1000
        elif u2 == "m/h":
            return v * 1000 
    
def fvol(v, u1, u2):
    if u1 == u2:
        return v
    elif u1 == "mm³":
        if u2 == "cm³":
            return v / 1000
        elif u2 == "dm³":
            return v / 1000000
        elif u2 == "m³":
            return v / 1000000000
        elif u2 == "mL":
            return v / 1000 
        elif u2 == "cL":
            return v / 10000 
        elif u2 == "dL":
            return v / 100000 
        elif u2 == "L":
            return v / 1000000 
    elif u1 == "cm³":
        if u2 == "mm³":
            return v * 1000
        elif u2 == "dm³":
            return v / 1000
        elif u2 == "m³":
            return v / 1000000
        elif u2 == "mL":
            return v 
        elif u2 == "cL":
            return v / 10
        elif u2 == "dL":
            return v / 100
        elif u2 == "L":
            return v / 1000
    elif u1 == "dm³":
        if u2 == "mm³":
            return v * 1000000
        elif u2 == "cm³":
            return v * 1000
        elif u2 == "m³":
            return v / 1000
        elif u2 == "mL":
            return v * 1000
        elif u2 == "cL":
            return v * 100
        elif u2 == "dL":
            return v * 10
        elif u2 == "L":
            return v
    elif u1 == "m³":
        if u2 == "mm³":
            return v * 1000000000
        elif u2 == "cm³":
            return v * 1000000
        elif u2 == "dm³":
            return v * 1000
        elif u2 == "mL":
            return v * 1000000
        elif u2 == "cL":
            return v * 100000
        elif u2 == "dL":
            return v * 10000
        elif u2 == "L":
            return v * 1000
    elif u1 == "mL":
        if u2 == "mm³":
            return v * 1000
        elif u2 == "cm³":
            return v
        elif u2 == "dm³":
            return v / 1000
        elif u2 == "m³":
            return v / 1000000
        elif u2 == "cL":
            return v / 10
        elif u2 == "dL":
            return v / 100
        elif u2 == "L":
            return v / 1000
    elif u1 == "cL":
        if u2 == "mm³":
            return v * 10000
        elif u2 == "cm³":
            return v * 10
        elif u2 == "dm³":
            return v / 100
        elif u2 == "m³":
            return v / 100000
        elif u2 == "mL":
            return v * 10
        elif u2 == "dL":
            return v / 10
        elif u2 == "L":
            return v / 100
    elif u1 == "dL":
        if u2 == "mm³":
            return v * 100000
        elif u2 == "cm³":
            return v * 100
        elif u2 == "dm³":
            return v / 10
        elif u2 == "m³":
            return v / 10000
        elif u2 == "mL":
            return v * 100
        elif u2 == "cL":
            return v * 10
        elif u2 == "L":
            return v / 10
    elif u1 == "L":
        if u2 == "mm³":
            return v * 1000000
        elif u2 == "cm³":
            return v * 1000
        elif u2 == "dm³":
            return v
        elif u2 == "m³":
            return v / 1000
        elif u2 == "mL":
            return v * 1000
        elif u2 == "cL":
            return v * 100
        elif u2 == "dL":
            return v * 10

def calc(v, u1, u2, con):
    if con == "Área":
        return farea(v, u1, u2)
    elif con == "Distância":
        return fdist(v, u1, u2)
    elif con == "Energia":
        return fene(v, u1, u2)
    elif con == "Massa":
        return fmass(v, u1, u2)
    elif con == "Potência":
        return fpot(v, u1, u2)
    elif con == "Temperatura":
        return ftemp(v, u1, u2)
    elif con == "Tempo":
        return ftime(v, u1, u2)
    elif con == "Velocidade":
        return fvel(v, u1, u2)
    elif con == "Volume":
        return fvol(v, u1, u2)