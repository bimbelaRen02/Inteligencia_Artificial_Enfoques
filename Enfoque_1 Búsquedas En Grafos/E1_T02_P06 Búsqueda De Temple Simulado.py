"""Planificación (2): Búsqueda Informada - Búsqueda de Temple Simulado.
La Búsqueda de Temple Simulado (Simulated Annealing) es una técnica de búsqueda estocástica que se inspira en el proceso físico de temple de los metales. 
A medida que el algoritmo avanza, la "temperatura" disminuye gradualmente, permitiendo que el algoritmo realice movimientos que inicialmente podrían ser desfavorables, 
lo que ayuda a evitar quedar atrapado en óptimos locales."""

import random #Para datos aleatorios
import math #Para usar operaciones matemáticas

def temple_simulado(grafo, inicio, objetivo, heuristica, temperatura_inicial=100, temperatura_minima=0.01, alpha=0.95, max_iter=1000):
    actual = inicio  #Nodo actual
    mejor_solucion = actual  #Mejor solución encontrada
    mejor_heuristica = heuristica(actual, objetivo)  #Heurística de la mejor solución
    temperatura = temperatura_inicial  #Temperatura inicial
    camino = [actual]  #Lista para almacenar el camino recorrido
    iteracion = 0

    while iteracion < max_iter and temperatura > temperatura_minima:
        vecinos = grafo.get(actual, [])  #Obtenemos los vecinos del nodo actual
        if not vecinos:
            break  #Si no hay vecinos, terminamos

        #Seleccionamos un vecino aleatorio
        vecino_aleatorio = random.choice(vecinos)

        #Calculamos la heurística del vecino
        heuristica_vecino = heuristica(vecino_aleatorio, objetivo)

        #Si el vecino es mejor o si se acepta un peor movimiento dependiendo de la temperatura
        delta_e = heuristica_vecino - heuristica(actual, objetivo)
        if delta_e < 0 or random.random() < math.exp(-delta_e / temperatura):
            actual = vecino_aleatorio  #Aceptamos el vecino
            camino.append(actual)  #Añadimos el nodo al camino

            #Actualizamos la mejor solución si es necesario
            if heuristica_vecino < mejor_heuristica:
                mejor_solucion = actual
                mejor_heuristica = heuristica_vecino

        #Reducimos la temperatura
        temperatura *= alpha
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

#Prueba de Búsqueda de Temple Simulado
camino = temple_simulado(grafo, inicio, objetivo, heuristica, temperatura_inicial=100, temperatura_minima=0.01, alpha=0.95, max_iter=1000)
print(f"Camino recorrido con Búsqueda de Temple Simulado desde {inicio} a {objetivo}: {camino}")