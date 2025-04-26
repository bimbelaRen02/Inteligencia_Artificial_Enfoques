"""Planificación (1): Búsqueda No Informada - Búsqueda Bidireccional. 
La Búsqueda Bidireccional busca simultáneamente desde el nodo inicial y desde el objetivo, 
encontrándose en algún punto intermedio, lo que puede reducir drásticamente el número de nodos explorados."""

from collections import deque

class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_arista(self, origen, destino):
        if origen not in self.nodos:
            self.nodos[origen] = []
        if destino not in self.nodos:
            self.nodos[destino] = []  #Se aseguran ambos nodos en el grafo
        self.nodos[origen].append(destino)
        self.nodos[destino].append(origen)  #Se asume grafo no dirigido para la búsqueda bidireccional

    def vecinos(self, nodo):
        return self.nodos.get(nodo, [])

def busqueda_bidireccional(grafo, inicio, objetivo):
    if inicio == objetivo:
        return [inicio]  #Caso trivial si el inicio es el objetivo

    #Inicialización de estructuras:
    frontera_inicio = deque([inicio])
    frontera_objetivo = deque([objetivo])
    padres_inicio = {inicio: None}
    padres_objetivo = {objetivo: None}

    while frontera_inicio and frontera_objetivo:
        #Expansión desde el inicio:
        nodo_actual_inicio = frontera_inicio.popleft()
        for vecino in grafo.vecinos(nodo_actual_inicio):
            if vecino not in padres_inicio:
                padres_inicio[vecino] = nodo_actual_inicio
                frontera_inicio.append(vecino)
                if vecino in padres_objetivo:
                    return reconstruir_camino(padres_inicio, padres_objetivo, vecino)

        #Expansión desde el objetivo
        nodo_actual_objetivo = frontera_objetivo.popleft()
        for vecino in grafo.vecinos(nodo_actual_objetivo):
            if vecino not in padres_objetivo:
                padres_objetivo[vecino] = nodo_actual_objetivo
                frontera_objetivo.append(vecino)
                if vecino in padres_inicio:
                    return reconstruir_camino(padres_inicio, padres_objetivo, vecino)

    return None  #No hay conexión

def reconstruir_camino(padres_inicio, padres_objetivo, nodo_encontrado):
    #Reconstruye el camino desde inicio al objetivo a través del nodo de encuentro
    camino_inicio = []
    actual = nodo_encontrado
    while actual:
        camino_inicio.append(actual)
        actual = padres_inicio[actual]
    camino_inicio.reverse()  #Invierte el camino desde el inicio al nodo encontrado

    camino_objetivo = []
    actual = padres_objetivo[nodo_encontrado]
    while actual:
        camino_objetivo.append(actual)
        actual = padres_objetivo[actual]

    return camino_inicio + camino_objetivo  #Combina los dos caminos

#Prueba del algoritmo
grafo = Grafo()
grafo.agregar_arista("A", "B")
grafo.agregar_arista("A", "C")
grafo.agregar_arista("B", "D")
grafo.agregar_arista("C", "E")
grafo.agregar_arista("D", "F")
grafo.agregar_arista("E", "F")

camino = busqueda_bidireccional(grafo, "A", "F")
print("Camino encontrado:", camino if camino else "No se encontró camino")

#Segunda prueba donde no hay conexión
grafo2 = Grafo()
grafo2.agregar_arista("X", "Y")
grafo2.agregar_arista("Y", "Z")
#Nodo "W" aislado
camino_inexistente = busqueda_bidireccional(grafo2, "X", "W")
print("Camino de nodos desconectados:", camino_inexistente if camino_inexistente else "No se encontró un camino")