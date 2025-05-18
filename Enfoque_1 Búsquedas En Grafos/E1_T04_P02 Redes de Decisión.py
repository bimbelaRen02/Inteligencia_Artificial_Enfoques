"""Utilidad y Toma de Decisiones - Redes de Decisión.
Las redes de decisión (influencia) combinan variables aleatorias, decisiones y utilidades
en un solo modelo gráfico. Permiten representar problemas de decisión bajo incertidumbre,
calculando la acción óptima al maximizar la utilidad esperada considerando la información disponible."""

#Importamos módulo para operaciones combinatorias
from itertools import product

#Definimos la red con variables, decisiones y nodo de utilidad
variables = {
    'clima': ['soleado', 'lluvioso'],  #Variable aleatoria (con incertidumbre)
    'decisión': ['bicicleta', 'auto']  #Nodo de decisión (acción que se elige)
}

#Distribución de probabilidad para el nodo de incertidumbre
P_clima = {
    'soleado': 0.7,  #70% de probabilidad de clima soleado
    'lluvioso': 0.3  #30% de probabilidad de lluvia
}

#Función de utilidad según el clima y la decisión
utilidad = {
    ('soleado', 'bicicleta'): 100,  #Alta utilidad en día soleado con bici
    ('soleado', 'auto'): 60,        #Menor utilidad por gasto innecesario
    ('lluvioso', 'bicicleta'): 10,  #Muy baja utilidad por incomodidad
    ('lluvioso', 'auto'): 80        #Alta utilidad por protección ante lluvia
}

#Función para calcular la utilidad esperada de una decisión
def utilidad_esperada(decisión):
    total = 0  #Acumulador
    for clima in variables['clima']:
        p = P_clima[clima]  #Probabilidad del clima
        u = utilidad[(clima, decisión)]  #Utilidad conjunta
        total += p * u  #Multiplicación ponderada
    return total  #Devuelve utilidad esperada total

#Mostrar utilidad esperada para cada acción posible
for d in variables['decisión']:
    ue = utilidad_esperada(d)
    print(f"Utilidad esperada de elegir '{d}': {ue}")  #Muestra cálculo

#Determinar la acción óptima
mejor_decisión = max(variables['decisión'], key=utilidad_esperada)  #Máxima utilidad
print(f"\nDecisión óptima: '{mejor_decisión}'")  #Resultado recomendado