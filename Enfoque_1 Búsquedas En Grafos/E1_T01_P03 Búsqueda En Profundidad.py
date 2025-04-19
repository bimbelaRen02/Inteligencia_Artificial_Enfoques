"""Planificación (1): Búsqueda No Informada - Búsqueda en Profundidad.
La Búsqueda en Profundidad (DFS) explora nodos en un grafo o árbol yendo tan lejos como
sea posible en una dirección antes de retroceder. Es útil cuando queremos recorrer
todos los nodos o cuando las soluciones están lejos del nodo raíz."""

class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_arista(self, origen, destino):
        if origen not in self.nodos:
            self.nodos[origen] = []
        self.nodos[origen].append(destino)

    def vecinos(self, nodo):
        return self.nodos.get(nodo, [])

def busqueda_profundidad(grafo, inicio, objetivo):
    pila = [(inicio, [inicio])]  # Lista como pila: contiene (nodo actual, camino hasta ahora)
    visitados = set()  # Registra los nodos ya visitados

    while pila:
        nodo_actual, camino = pila.pop()  # Extrae el nodo más recientemente insertado (LIFO)
        print(f"Explorando nodo: {nodo_actual}")  # Mostrar el nodo que se está visitando

        if nodo_actual == objetivo:
            print(f"Objetivo '{objetivo}' encontrado.")
            return camino  # Si llegamos al objetivo, regresamos el camino

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)  # Marca el nodo como visitado

            for vecino in reversed(grafo.vecinos(nodo_actual)):
                pila.append((vecino, camino + [vecino]))  # Agrega vecinos no visitados con su camino

    print(f"No se encontró un camino de '{inicio}' a '{objetivo}'.")
    return None  # Si no se encuentra un camino

#Prueba del algoritmo DFS
grafo = Grafo()
grafo.agregar_arista("A", "B")
grafo.agregar_arista("A", "C")
grafo.agregar_arista("B", "D")
grafo.agregar_arista("C", "E")
grafo.agregar_arista("D", "F")
grafo.agregar_arista("E", "F")

camino = busqueda_profundidad(grafo, "A", "F")
print("Camino encontrado:", camino)