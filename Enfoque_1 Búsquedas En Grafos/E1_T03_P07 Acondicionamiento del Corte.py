"""Planificación (3): Satisfacción De Restricciones - Acondicionamiento del Corte
Este algoritmo es útil para resolver problemas de satisfacción de restricciones (CSP)
que no son árboles (i.e., tienen ciclos). La idea principal es:
1. Identificar un conjunto de corte (cutset): un conjunto pequeño de variables que,
   al fijarse (condicionarse), convierten el grafo de restricciones en un árbol.
2. Enumerar todas las combinaciones posibles de valores para las variables del cutset.
3. Para cada combinación, usar un algoritmo eficiente de CSP en árboles (como búsqueda hacia adelante)
   para resolver el problema condicionado."""

import itertools  # Para generar todas las combinaciones posibles
import random     # Para asignaciones aleatorias

# Definimos el problema (grafo de coloreo con ciclos)
variables = ['A', 'B', 'C', 'D']  # Variables del CSP
dominios = {var: [1, 2, 3] for var in variables}  # Dominios posibles

# Restricciones binarias (cada par debe tener colores distintos)
restricciones = {
    'A': [('B', lambda a, b: a != b), ('C', lambda a, c: a != c)],
    'B': [('A', lambda b, a: b != a), ('C', lambda b, c: b != c), ('D', lambda b, d: b != d)],
    'C': [('A', lambda c, a: c != a), ('B', lambda c, b: c != b), ('D', lambda c, d: c != d)],
    'D': [('B', lambda d, b: d != b), ('C', lambda d, c: d != c)]
}

# Conjunto de corte (cutset) elegido manualmente
cutset = ['C']  # Al fijar C, el grafo resultante se convierte en árbol

# Función para verificar si una asignación cumple las restricciones
def es_consistente(var, valor, asignacion):  # Verifica consistencia local
    for vecino, restriccion in restricciones[var]:  # Revisa cada restricción de la variable
        if vecino in asignacion:  # Si el vecino ya fue asignado
            if not restriccion(valor, asignacion[vecino]):  # Verifica la restricción
                return False  # Si no cumple, retorna False
    return True  # Si cumple con todas, retorna True

# Búsqueda hacia adelante para árboles (simplificada)
def resolver_arbol(asignacion_parcial):  # Asignación parcial que fija el cutset
    asignacion = asignacion_parcial.copy()  # Copia la asignación parcial
    no_asignadas = [v for v in variables if v not in asignacion]  # Variables restantes

    def backtrack():  # Algoritmo de backtracking clásico
        if len(asignacion) == len(variables):  # Si ya se asignaron todas las variables
            return asignacion  # Retorna solución completa
        var = no_asignadas[len(asignacion_parcial)]  # Selecciona siguiente variable
        for valor in dominios[var]:  # Intenta cada valor posible
            if es_consistente(var, valor, asignacion):  # Verifica si es consistente
                asignacion[var] = valor  # Asigna el valor
                resultado = backtrack()  # Llama recursivamente
                if resultado is not None:  # Si se encontró solución
                    return resultado  # Retorna la solución
                del asignacion[var]  # Si no, deshace la asignación
        return None  # Si ninguna asignación funciona, retorna None

    return backtrack()  # Llama al backtracking

# Algoritmo principal de acondicionamiento del corte
def cutset_conditioning(variables, dominios, restricciones, cutset):
    soluciones = []  # Guarda soluciones encontradas

    # Genera todas las combinaciones posibles para el cutset
    combinaciones_cutset = list(itertools.product(*[dominios[var] for var in cutset]))  # Producto cartesiano

    for combinacion in combinaciones_cutset:  # Recorre cada combinación
        asignacion_cutset = dict(zip(cutset, combinacion))  # Asignación parcial al cutset

        if all(es_consistente(var, asignacion_cutset[var], asignacion_cutset) for var in cutset):  # Verifica si la asignación es consistente entre sí
            solucion = resolver_arbol(asignacion_cutset)  # Resuelve el resto del árbol
            if solucion:  # Si se encontró solución válida
                soluciones.append(solucion)  # Agrega a la lista de soluciones

    if soluciones:  # Si hay soluciones
        print(f"Se encontraron {len(soluciones)} soluciones posibles.")  # Muestra el total
        return soluciones[0]  # Retorna una (la primera)
    else:
        print("No se encontró solución.")  # Si ninguna combinación funcionó
        return None  # Retorna None

# Ejecutar el algoritmo
solucion = cutset_conditioning(variables, dominios, restricciones, cutset)  # Ejecuta con el cutset C
print("Solución encontrada:", solucion)  # Muestra la solución obtenida