"""Planificación (2): Búsqueda Informada - Búsqueda de Ascensión de Colinas.
La Búsqueda de Ascensión de Colinas consiste en moverse iterativamente hacia el vecino más prometedor, 
según una función heurística, con la esperanza de encontrar la cima (óptimo local).

Se incluye también una versión de Ascensión de Colinas Aleatoria para ilustrar 
cómo se puede evitar quedar atrapado en óptimos locales seleccionando vecinos al azar, 
mejorando así la exploración del espacio de búsqueda en problemas más complejos."""

import random  #Importamos random para operaciones aleatorias

def ascension_colinas(grafo, inicio, objetivo, heuristica):
    actual = inicio  #Inicializamos el nodo actual como el nodo de inicio
    camino = [actual]  #Lista para guardar el camino recorrido

    while actual != objetivo:
        vecinos = grafo.get(actual, [])  #Obtenemos los vecinos del nodo actual
        if not vecinos:
            break  #Si no hay vecinos, terminamos (atrapados en un máximo local)
        vecino_mejor = min(vecinos, key=lambda x: heuristica(x, objetivo))  #Seleccionamos el mejor vecino según la heurística
        if heuristica(vecino_mejor, objetivo) >= heuristica(actual, objetivo):
            break  #Si no encontramos un mejor vecino, terminamos
        actual = vecino_mejor  #Actualizamos el nodo actual al mejor vecino
        camino.append(actual)  #Agregamos el nuevo nodo al camino
    return camino  #Devolvemos el camino recorrido

def ascension_colinas_aleatoria(grafo, inicio, objetivo, heuristica):
    actual = inicio  #Inicializamos el nodo actual como el nodo de inicio
    camino = [actual]  #Lista para guardar el camino recorrido

    while actual != objetivo:
        vecinos = grafo.get(actual, [])  #Obtenemos los vecinos del nodo actual
        if not vecinos:
            break  #Si no hay vecinos, terminamos
        mejor_valor = heuristica(actual, objetivo)  #Calculamos la heurística del nodo actual
        mejores_vecinos = [n for n in vecinos if heuristica(n, objetivo) < mejor_valor]  #Filtramos solo vecinos mejores
        if not mejores_vecinos:
            break  #Si no hay vecinos mejores, terminamos
        actual = random.choice(mejores_vecinos)  #Seleccionamos aleatoriamente uno de los mejores vecinos
        camino.append(actual)  #Agregamos el nuevo nodo al camino
    return camino  #Devolvemos el camino recorrido

def heuristica(nodo, objetivo):
    return abs(ord(nodo) - ord(objetivo))  #Heurística simple basada en distancia alfabética

#Prueba del algoritmo:
grafo = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": ["G"],
    "G": []
}

inicio = "A"
objetivo = "G"

#Prueba de Ascensión de Colinas
camino = ascension_colinas(grafo, inicio, objetivo, heuristica)
print(f"Camino encontrado con Ascensión de Colinas desde {inicio} a {objetivo}: {camino}")

#Prueba de Ascensión de Colinas Aleatoria
camino_aleatorio = ascension_colinas_aleatoria(grafo, inicio, objetivo, heuristica)
print(f"Camino encontrado con Ascensión de Colinas Aleatoria desde {inicio} a {objetivo}: {camino_aleatorio}")