"""Planificación (2): Búsqueda Informada - Búsqueda Voraz Primero el Mejor.
La Búsqueda Voraz Primero el Mejor selecciona el nodo que parece más cercano al objetivo según una heurística, 
sin considerar el costo acumulado del camino recorrido."""

import heapq  #Importamos heapq para manejar una cola de prioridad basada en la heurística

def busqueda_voraz_primero_mejor(grafo, inicio, objetivo, heuristica):
    frontera = []  #Inicializamos la frontera como una lista vacía
    heapq.heappush(frontera, (heuristica(inicio, objetivo), inicio))  #Agregamos el nodo inicial con su valor heurístico
    visitados = set()  #Conjunto para registrar los nodos visitados

    while frontera:
        _, actual = heapq.heappop(frontera)  #Extraemos el nodo con menor valor heurístico
        if actual == objetivo:
            return True  #Retornamos éxito si llegamos al objetivo
        visitados.add(actual)  #Marcamos el nodo actual como visitado
        for vecino in grafo.get(actual, []):
            if vecino not in visitados:
                heapq.heappush(frontera, (heuristica(vecino, objetivo), vecino))  #Agregamos vecinos no visitados a la frontera
    return False  #Si la frontera se vacía sin encontrar el objetivo

def heuristica(nodo, objetivo):
    return abs(ord(nodo) - ord(objetivo))  #Heurística basada en la distancia alfabética

#Prueba del algoritmo:
grafo = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

inicio = "A"
objetivo = "F"

encontrado = busqueda_voraz_primero_mejor(grafo, inicio, objetivo, heuristica)
print(f"¿Se encontró el objetivo {objetivo} desde {inicio}? {encontrado}")