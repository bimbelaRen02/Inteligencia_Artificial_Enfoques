"""Planificación (1): Búsqueda No Informada - Búsqueda en Profundidad Limitada. 
La Búsqueda en Profundidad Limitada es una variante de la búsqueda en profundidad que impone un límite de profundidad,
evitando así exploraciones infinitas en grafos o árboles cíclicos. Es útil cuando se tiene una estimación del "profundómetro"
hasta la solución o cuando se quiere controlar el costo computacional."""

class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_arista(self, origen, destino):
        if origen not in self.nodos:
            self.nodos[origen] = []
        self.nodos[origen].append(destino)

    def vecinos(self, nodo):
        return self.nodos.get(nodo, [])

def busqueda_profundidad_limitada(grafo, inicio, objetivo, limite):
    def dfs_limitado(nodo_actual, camino, profundidad):
        print(f"Explorando nodo: {nodo_actual} a profundidad {profundidad}")  # Muestra el nodo actual y su profundidad

        if nodo_actual == objetivo:
            print(f"Objetivo '{objetivo}' encontrado.")
            return camino
        
        if profundidad >= limite:
            return None  # Si se alcanza el límite, se detiene esta rama

        for vecino in grafo.vecinos(nodo_actual):
            if vecino not in camino:  # Evita ciclos simples
                resultado = dfs_limitado(vecino, camino + [vecino], profundidad + 1)
                if resultado:
                    return resultado  # Devuelve la solución si se encontró

        return None  # Si no hay solución en esta rama

    return dfs_limitado(inicio, [inicio], 0)

#Prueba del algoritmo
grafo = Grafo()
grafo.agregar_arista("A", "B")
grafo.agregar_arista("A", "C")
grafo.agregar_arista("B", "D")
grafo.agregar_arista("C", "E")
grafo.agregar_arista("D", "F")
grafo.agregar_arista("E", "F")

limite = 3
camino = busqueda_profundidad_limitada(grafo, "A", "F", limite)
print("Camino encontrado:", camino if camino else "No se encontró camino dentro del límite")

#Segunda prueba con límite muy bajo
limite_bajo = 2
camino_bajo = busqueda_profundidad_limitada(grafo, "A", "F", limite_bajo) #Veremos como retrocede de A-B a A-C cuando excede el límite
print("Camino encontrado (límite 2):", camino_bajo if camino_bajo else "No se encontró camino dentro del límite")