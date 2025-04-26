"""Planificación (1): Búsqueda No Informada - Búsqueda en Grafos. 
La Búsqueda en Grafos evita ciclos y la expansión repetida de nodos ya visitados, 
lo que la hace más eficiente que la búsqueda en árboles para entornos con caminos redundantes."""

from collections import deque

class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_arista(self, origen, destino):
        if origen not in self.nodos:
            self.nodos[origen] = []
        if destino not in self.nodos:
            self.nodos[destino] = []
        self.nodos[origen].append(destino)

    def vecinos(self, nodo):
        return self.nodos.get(nodo, [])

def busqueda_en_grafo(grafo, inicio, objetivo):
    frontera = deque([inicio])  #Cola para nodos a explorar
    visitados = set([inicio])  #Conjunto para nodos ya explorados
    padres = {inicio: None}  #Registro de padres para reconstruir camino

    while frontera:
        actual = frontera.popleft()
        if actual == objetivo:
            return reconstruir_camino(padres, inicio, objetivo)
        for vecino in grafo.vecinos(actual):
            if vecino not in visitados:
                visitados.add(vecino)
                padres[vecino] = actual
                frontera.append(vecino)
    return None  #No se encontró camino

def reconstruir_camino(padres, inicio, objetivo):
    camino = []
    actual = objetivo
    while actual is not None:
        camino.append(actual)
        actual = padres[actual]
    camino.reverse()  #El camino se reconstruye desde el objetivo hacia el inicio
    return camino

#Prueba del algoritmo
grafo = Grafo()
grafo.agregar_arista("A", "B")
grafo.agregar_arista("A", "C")
grafo.agregar_arista("B", "D")
grafo.agregar_arista("C", "D")
grafo.agregar_arista("D", "E")
grafo.agregar_arista("E", "B")  #Ciclo B->D->E->B

camino = busqueda_en_grafo(grafo, "A", "E")
print("Camino encontrado:", camino if camino else "No se encontró camino")

#Prueba donde no existe conexión:
grafo2 = Grafo()
grafo2.agregar_arista("X", "Y")
grafo2.agregar_arista("Y", "Z")
#Nodo aislado "W":
camino_inexistente = busqueda_en_grafo(grafo2, "X", "W")
print("Camino encontrado (nodos desconectados):", camino_inexistente if camino_inexistente else "No se encontró camino")