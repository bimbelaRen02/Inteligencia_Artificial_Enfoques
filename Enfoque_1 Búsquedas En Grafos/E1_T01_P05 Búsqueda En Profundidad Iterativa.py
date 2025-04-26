"""Planificación (1): Búsqueda No Informada - Búsqueda en Profundidad Iterativa. 
La Búsqueda en Profundidad Iterativa combina los beneficios de la búsqueda en profundidad (bajo uso de memoria) 
y la búsqueda en anchura (garantía de encontrar la solución más cercana), realizando múltiples búsquedas en 
profundidad limitada aumentando progresivamente el límite."""

class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_arista(self, origen, destino):
        if origen not in self.nodos:
            self.nodos[origen] = []
        self.nodos[origen].append(destino)

    def vecinos(self, nodo):
        return self.nodos.get(nodo, [])

def busqueda_profundidad_iterativa(grafo, inicio, objetivo, limite_maximo):
    def dfs_limitado(nodo_actual, camino, profundidad, limite):
        print(f"Explorando nodo: {nodo_actual} a profundidad {profundidad}")  # Imprime el nodo actual y su profundidad
        if nodo_actual == objetivo:
            print(f"Objetivo '{objetivo}' encontrado.")
            return camino
        
        if profundidad >= limite:
            return None  # Si alcanza el límite actual, se detiene en esta rama

        for vecino in grafo.vecinos(nodo_actual):
            if vecino not in camino:
                resultado = dfs_limitado(vecino, camino + [vecino], profundidad + 1, limite)
                if resultado:
                    return resultado

        return None

    for limite in range(limite_maximo + 1):
        print(f"\nIniciando búsqueda con límite de profundidad: {limite}")  # Indica el nuevo límite en esta iteración
        resultado = dfs_limitado(inicio, [inicio], 0, limite)
        if resultado:
            return resultado

    return None  # No se encontró solución dentro del límite máximo

#Prueba del algoritmo
grafo = Grafo()
grafo.agregar_arista("A", "B")
grafo.agregar_arista("A", "C")
grafo.agregar_arista("B", "D")
grafo.agregar_arista("C", "E")
grafo.agregar_arista("D", "F")
grafo.agregar_arista("E", "F")

limite_maximo = 5
camino = busqueda_profundidad_iterativa(grafo, "A", "F", limite_maximo)
print("Camino encontrado:", camino if camino else "No se encontró camino dentro del límite máximo")

# Segunda prueba con límite demasiado bajo
limite_bajo = 2
camino_bajo = busqueda_profundidad_iterativa(grafo, "A", "F", limite_bajo)
print("Camino de límite bajo:", camino_bajo if camino_bajo else "No se encontró camino dentro del límite máximo")