"""Planificación (2): Búsqueda Informada - Búsquedas A* y AO*.
La búsqueda A* combina el costo del camino recorrido y una estimación
heurística del costo restante hasta el objetivo, buscando siempre la
solución más barata. AO* se utiliza en grafos AND-OR donde pueden
existir decisiones compuestas."""

import heapq  #Importamos heapq para manejar la cola de prioridad basada en el costo total estimado

def busqueda_a_estrella(grafo, inicio, objetivo, heuristica):
    frontera = []  #Inicializamos la frontera como una lista vacía
    heapq.heappush(frontera, (0 + heuristica(inicio, objetivo), 0, inicio, [inicio]))  #Costo estimado, costo real, nodo, camino
    visitados = set()  #Conjunto para registrar los nodos visitados

    while frontera:
        estimado_total, costo_actual, actual, camino = heapq.heappop(frontera)  #Sacamos el nodo con menor costo estimado
        if actual == objetivo:
            return camino  #Retornamos el camino completo hasta el objetivo
        visitados.add(actual)  #Marcamos el nodo actual como visitado
        for vecino, costo in grafo.get(actual, []):
            if vecino not in visitados:
                nuevo_costo = costo_actual + costo  #Actualizamos el costo real
                estimado = nuevo_costo + heuristica(vecino, objetivo)  #Calculamos el nuevo costo estimado
                heapq.heappush(frontera, (estimado, nuevo_costo, vecino, camino + [vecino]))  #Agregamos a la frontera
    return None  #Si la frontera se vacía sin encontrar el objetivo

def heuristica(nodo, objetivo):
    return abs(ord(nodo) - ord(objetivo))  #Heurística simple basada en la distancia alfabética

#Prueba del algoritmo A*:
grafo = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 5), ("E", 2)],
    "C": [("F", 3)],
    "D": [],
    "E": [("F", 1)],
    "F": []
}

inicio = "A"
objetivo = "F"

camino = busqueda_a_estrella(grafo, inicio, objetivo, heuristica)
print(f"Camino encontrado con A* de {inicio} a {objetivo}: {camino}")

#-------------------------------------------------------

#Implementación de AO* para grafos AND-OR:
def busqueda_ao_estrella(nodo, grafo, heuristica):
    solucion = {}  #Diccionario para almacenar las mejores decisiones
    visitados = set()  #Conjunto para registrar nodos visitados

    def ao_star(actual):
        if actual not in grafo or not grafo[actual]:
            solucion[actual] = []  #Nodo terminal
            return 0
        if actual in visitados:
            return heuristica(actual)  #Ciclo detectado
        visitados.add(actual)
        mejor_costo = float('inf') #Costo inicial transformado a infinito
        mejor_subarbol = []
        for opcion in grafo[actual]:
            costo_opcion = sum(heuristica(hijo) for hijo in opcion)  #Costo estimado de esta opción
            if costo_opcion < mejor_costo:
                mejor_costo = costo_opcion
                mejor_subarbol = opcion
        solucion[actual] = mejor_subarbol
        for hijo in mejor_subarbol:
            ao_star(hijo)
        return mejor_costo

    ao_star(nodo)
    return solucion

#Prueba del algoritmo AO*:
grafo_and_or = {
    "A": [["B", "C"], ["D"]],
    "B": [["E"], ["F"]],
    "C": [["G"]],
    "D": [["G"]],
    "E": [],
    "F": [],
    "G": []
}

solucion = busqueda_ao_estrella("A", grafo_and_or, lambda x: 1)  #Usamos una heurística constante por simplicidad
print(f"Estructura de solución AO* desde A: {solucion}")