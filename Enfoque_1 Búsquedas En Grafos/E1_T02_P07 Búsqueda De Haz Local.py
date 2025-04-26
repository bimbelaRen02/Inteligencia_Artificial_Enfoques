"""Planificación (2): Búsqueda Informada - Búsqueda de Haz Local.
La Búsqueda de Haz Local (Local Beam Search) es una variante de la búsqueda en amplitud en la que, en lugar de explorar todos los nodos a un mismo nivel, 
se mantiene un conjunto de nodos y se seleccionan los mejores nodos de entre ellos en cada paso. La idea es reducir la cantidad de nodos a explorar al centrarse 
en los más prometedores, pero sin perder la capacidad de explorar diferentes caminos."""

import random #Para usar operaciones aleatorias

def busqueda_haz_local(grafo, inicio, objetivo, heuristica, k=2, max_iter=100):
    frontera = [(inicio, [inicio])]  #Inicializamos la frontera con el nodo de inicio y el camino
    mejor_solucion = (inicio, [inicio])  #Mejor solución encontrada (nodo, camino)
    mejor_heuristica = heuristica(inicio, objetivo)  #Heurística de la mejor solución encontrada
    
    iteracion = 0
    while iteracion < max_iter:
        siguiente_frontera = []
        
        #Expandimos todos los nodos de la frontera actual
        for nodo, camino in frontera:
            vecinos = grafo.get(nodo, [])  #Obtenemos los vecinos del nodo actual
            for vecino in vecinos:
                siguiente_frontera.append((vecino, camino + [vecino]))  #Agregamos al camino

        #Seleccionamos los mejores k nodos según la heurística
        siguiente_frontera = sorted(siguiente_frontera, key=lambda x: heuristica(x[0], objetivo))
        frontera = siguiente_frontera[:k]  #Mantenemos solo los mejores k nodos

        #Actualizamos la mejor solución
        for nodo, camino in frontera:
            h = heuristica(nodo, objetivo)
            if h < mejor_heuristica:
                mejor_solucion = (nodo, camino)
                mejor_heuristica = h
        
        iteracion += 1

    return mejor_solucion  #Devolvemos la mejor solución encontrada (nodo, camino)

def heuristica(nodo, objetivo):
    return abs(ord(nodo) - ord(objetivo))  #Heurística simple basada en distancia alfabética

#Prueba del algoritmo
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

#Prueba de Búsqueda de Haz Local
mejor_solucion = busqueda_haz_local(grafo, inicio, objetivo, heuristica, k=2, max_iter=100)
print(f"Mejor solución encontrada con Búsqueda de Haz Local desde {inicio} a {objetivo}: {mejor_solucion[1]}")