"""Planificación (1):
Búsqueda No Informada
La Búsqueda en Anchura (Breadth-First Search, BFS) es un algoritmo de búsqueda no informada
que explora primero los nodos más cercanos al nodo inicial antes de ir más profundo. Se
implementa típicamente usando una cola FIFO."""

from collections import deque

def bfs(grafo, inicio, objetivo): #Definir la función bfs con los parámetros grafo, inicio y objetivo
    visitados = set()
    cola = deque([[inicio]])  # Cola de caminos, no solo nodos

    if inicio == objetivo:
        return [inicio]

    while cola:
        camino = cola.popleft()  # Extraer el camino más antiguo
        nodo = camino[-1]  # Último nodo del camino actual

        if nodo not in visitados:
            vecinos = grafo.get(nodo, [])
            for vecino in vecinos:
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                if vecino == objetivo:
                    return nuevo_camino
                cola.append(nuevo_camino)
            visitados.add(nodo)

    return None  # Si no se encuentra el objetivo

#Prueba del algoritmo BFS
grafo = { #Definimos el grafo como un diccionario
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

inicio = 'A'
objetivo = 'F'

camino = bfs(grafo, inicio, objetivo)
print(f"Camino encontrado: {camino}")