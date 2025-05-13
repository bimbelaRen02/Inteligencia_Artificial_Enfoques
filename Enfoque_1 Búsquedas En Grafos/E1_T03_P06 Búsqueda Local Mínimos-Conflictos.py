"""Planificación (3): Satisfacción De Restricciones - Búsqueda Local: Mínimos-Conflictos
Este algoritmo se aplica a problemas de satisfacción de restricciones (CSP),
como el coloreo de grafos, el problema de las N-reinas o el Sudoku. La idea
central es comenzar con una asignación aleatoria y luego, mientras existan
conflictos (restricciones no satisfechas), seleccionar una variable conflictiva
y asignarle el valor que genere menos conflictos."""

import random  # Importa el módulo random para selecciones aleatorias

# Variables y dominios posibles
variables = ['A', 'B', 'C']  # Lista de variables
dominios = {var: [1, 2, 3] for var in variables}  # Cada variable puede tomar los valores 1, 2 o 3

# Restricciones binarias de desigualdad (cada par debe tener valores distintos)
restricciones = {
    'A': [('B', lambda a, b: a != b), ('C', lambda a, c: a != c)],
    'B': [('A', lambda b, a: b != a), ('C', lambda b, c: b != c)],
    'C': [('A', lambda c, a: c != a), ('B', lambda c, b: c != b)]
}

# Función para contar cuántos conflictos genera asignar cierto valor a una variable
def contar_conflictos(var, valor, asignacion):
    conflictos = 0  # Inicializa el contador de conflictos
    for vecino, restriccion in restricciones[var]:  # Recorre los vecinos con restricciones
        if vecino in asignacion:  # Solo si ya se ha asignado ese vecino
            if not restriccion(valor, asignacion[vecino]):  # Si no cumple la restricción
                conflictos += 1  # Aumenta el número de conflictos
    return conflictos  # Devuelve el total de conflictos para ese valor

# Algoritmo principal de mínimos-conflictos
def min_conflicts(variables, dominios, restricciones, max_iter=1000):
    asignacion = {var: random.choice(dominios[var]) for var in variables}  # Asignación aleatoria inicial
    
    for i in range(max_iter):  # Bucle principal de iteraciones
        conflictos_totales = sum(  # Suma los conflictos totales en la asignación actual
            contar_conflictos(var, valor, asignacion)
            for var, valor in asignacion.items()
        )
        if conflictos_totales == 0:  # Si no hay conflictos, es una solución válida
            print(f"Solución encontrada en {i} iteraciones.")  # Muestra éxito
            return asignacion  # Retorna la solución encontrada

        # Selecciona una variable conflictiva al azar
        variables_conflictivas = [
            var for var in variables
            if contar_conflictos(var, asignacion[var], asignacion) > 0
        ]
        var = random.choice(variables_conflictivas)  # Elige una variable con conflictos

        # Busca el valor con el menor número de conflictos para esa variable
        min_conf = float('inf')  # Inicializa el mínimo de conflictos como infinito
        mejor_valor = None  # Valor óptimo aún no asignado
        for valor in dominios[var]:  # Recorre todos los valores posibles
            conflictos = contar_conflictos(var, valor, asignacion)  # Cuenta conflictos
            if conflictos < min_conf:  # Si este valor genera menos conflictos
                min_conf = conflictos  # Actualiza el mínimo
                mejor_valor = valor  # Guarda el mejor valor

        asignacion[var] = mejor_valor  # Asigna el nuevo valor con menos conflictos

    print("No se encontró solución dentro del límite de iteraciones.")  # Si no hay solución
    return None  # Retorna None en caso de fallo

# Ejecutar el algoritmo
solucion = min_conflicts(variables, dominios, restricciones)  # Ejecuta con las variables dadas
print("Solución final:", solucion)  # Imprime la solución obtenida