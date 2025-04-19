"""Planificación (1): Búsqueda No Informada - Búsqueda en Anchura De Coste Uniforme.
La Búsqueda en Anchura de Costo Uniforme (Uniform Cost Search, UCS). Este tipo de
búsqueda prioriza los caminos con menor costo acumulado, por lo que se utiliza una
cola de prioridad."""

import heapq

class Grafo: #Definimos la clase Grafo
    def __init__(self): #Definimos el método inicializador
        self.nodos = {}

    def agregar_arista(self, origen, destino, costo): # Añade la arista de 'origen' a 'destino' con el costo especificado
        if origen not in self.nodos:
            self.nodos[origen] = []
        self.nodos[origen].append((destino, costo))

    def vecinos(self, nodo): # Regresa la lista de vecinos y sus costos desde el nodo dado
        return self.nodos.get(nodo, [])

def busqueda_costo_uniforme(grafo, inicio, objetivo): # Cola de prioridad: (costo acumulado, nodo actual, camino recorrido)
    frontera = [(0, inicio, [inicio])]
    heapq.heapify(frontera)  # Asegura que se mantenga ordenada por costo

    visitados = set()  # Para evitar ciclos

    while frontera:
        costo_actual, nodo_actual, camino = heapq.heappop(frontera)

        if nodo_actual in visitados:
            continue
        visitados.add(nodo_actual)

        # Si encontramos el objetivo, retornamos el camino y su costo
        if nodo_actual == objetivo:
            return camino, costo_actual

        # Expandimos vecinos y agregamos a la frontera
        for vecino, costo in grafo.vecinos(nodo_actual):
            if vecino not in visitados:
                nuevo_costo = costo_actual + costo
                heapq.heappush(frontera, (nuevo_costo, vecino, camino + [vecino]))

    return None, float('inf')  # Si no se encuentra un camino

#Prueba del algoritmo UCS
grafo = Grafo()
grafo.agregar_arista("A", "B", 1)
grafo.agregar_arista("A", "C", 5)
grafo.agregar_arista("B", "D", 2)
grafo.agregar_arista("C", "D", 1)
grafo.agregar_arista("D", "E", 3)

camino, costo = busqueda_costo_uniforme(grafo, "A", "E")
print("Camino encontrado:", camino)
print("Costo total:", costo)