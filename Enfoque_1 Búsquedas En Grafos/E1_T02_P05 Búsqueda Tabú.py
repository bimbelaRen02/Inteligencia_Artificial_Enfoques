"""
Planificación (2): Búsqueda Informada - Búsqueda Tabú.
La Búsqueda Tabú es una metaheurística que utiliza un enfoque de búsqueda local 
en el que se mantiene una lista de soluciones "tabú" (prohibidas) para evitar volver a explorar áreas ya visitadas. 
Esto ayuda a evitar quedar atrapado en óptimos locales, permitiendo explorar más eficientemente el espacio de soluciones.
"""

import random #Importamos random para operaciones aleatorias

def busqueda_tabu(grafo, inicio, objetivo, heuristica, max_iter=100, tamano_tabu=5): #Definimos la función de búsqueda tabú
    actual = inicio  #Nodo inicial
    mejor_solucion = actual  #Solución inicial
    mejor_heuristica = heuristica(actual, objetivo)  #Heurística de la mejor solución
    tabu_list = []  #Lista de soluciones tabú
    camino = [actual]  #Lista para almacenar el camino recorrido
    iteracion = 0

    while iteracion < max_iter:
        vecinos = grafo.get(actual, [])  #Obtenemos los vecinos del nodo actual
        if not vecinos:
            break  #Si no hay vecinos, terminamos

        # Filtramos los vecinos tabú
        vecinos_viables = [n for n in vecinos if n not in tabu_list]

        if not vecinos_viables:
            break  #Si no hay vecinos viables, terminamos

        # Seleccionamos el vecino con la mejor heurística (mínima)
        mejor_vecino = min(vecinos_viables, key=lambda x: heuristica(x, objetivo))

        if heuristica(mejor_vecino, objetivo) < mejor_heuristica:
            mejor_solucion = mejor_vecino  #Actualizamos la mejor solución
            mejor_heuristica = heuristica(mejor_vecino, objetivo)

        tabu_list.append(mejor_vecino)  #Añadimos el vecino actual a la lista tabú
        if len(tabu_list) > tamano_tabu:  #Si la lista tabú supera el tamaño máximo
            tabu_list.pop(0)  #Eliminamos el primer elemento de la lista tabú

        actual = mejor_vecino  #Nos movemos al mejor vecino
        camino.append(actual)  #Añadimos el nodo actual al camino recorrido
        iteracion += 1

    return camino  #Devolvemos el camino completo

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

#Prueba de Búsqueda Tabú
camino = busqueda_tabu(grafo, inicio, objetivo, heuristica, max_iter=50, tamano_tabu=3)
print(f"Camino recorrido con Búsqueda Tabú desde {inicio} a {objetivo}: {camino}")