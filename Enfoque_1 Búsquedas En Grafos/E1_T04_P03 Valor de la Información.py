"""Utilidad y Toma de Decisiones - Valor de la Información.
El Valor de la Información (VOI) mide cuánto vale obtener información adicional antes de tomar una decisión.
Permite calcular si vale la pena adquirir datos (por ejemplo, diagnósticos o sensores) al comparar
la utilidad esperada con y sin dicha información."""

#Importamos módulo para combinaciones
from itertools import product

#Definimos variables del problema
climas = ['soleado', 'lluvioso']  #Estados posibles del mundo
decisiones = ['bicicleta', 'auto']  #Acciones posibles

#Probabilidades del clima (sin información adicional)
P_clima = {
    'soleado': 0.7,
    'lluvioso': 0.3
}

#Función de utilidad según clima y decisión
utilidad = {
    ('soleado', 'bicicleta'): 100,
    ('soleado', 'auto'): 60,
    ('lluvioso', 'bicicleta'): 10,
    ('lluvioso', 'auto'): 80
}

#Cálculo de utilidad esperada sin información adicional
def utilidad_esperada_sin_info():
    utilidades = {}
    for d in decisiones:
        total = 0
        for c in climas:
            total += P_clima[c] * utilidad[(c, d)]  #Ponderamos por probabilidad
        utilidades[d] = total
    mejor_utilidad = max(utilidades.values())  #Elegimos la mejor decisión
    return mejor_utilidad

#Cálculo de utilidad esperada con información perfecta
def utilidad_esperada_con_info():
    total = 0
    for c in climas:
        #Si sabemos que el clima será "c", elegimos la mejor decisión en ese caso
        mejor_utilidad = max(utilidad[(c, d)] for d in decisiones)
        total += P_clima[c] * mejor_utilidad  #Ponderamos por probabilidad del clima
    return total

#Cálculo del valor de la información perfecta
voi = utilidad_esperada_con_info() - utilidad_esperada_sin_info()

#Mostrar resultados
print(f"Utilidad esperada sin información: {utilidad_esperada_sin_info()}")  #Decisión sin datos adicionales
print(f"Utilidad esperada con información perfecta: {utilidad_esperada_con_info()}")  #Decisión con datos perfectos
print(f"Valor de la información perfecta: {voi}")  #Valor económico de tener información anticipada