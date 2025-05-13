"""Planificación (2): Búsqueda Informada - Búsqueda Online.
La Búsqueda Online es utilizada cuando el agente no conoce por completo el entorno
desde el inicio y debe ir descubriéndolo conforme avanza. Es común en escenarios
como robots exploradores o videojuegos. El agente actúa en tiempo real, basando sus
decisiones en la información adquirida hasta el momento."""

from collections import defaultdict, deque

class EntornoDesconocido:
    def __init__(self):
        self.mapa_real = defaultdict(list)  #Grafo del entorno real, que el agente irá descubriendo
        self.explorado = set()  #Nodos que el agente ya ha visitado
        self.posicion_actual = None  #Nodo en el que se encuentra actualmente el agente

    def agregar_arista(self, origen, destino):
        self.mapa_real[origen].append(destino)  #Agrega una conexión del nodo origen al nodo destino
        self.mapa_real[destino].append(origen)  #Agrega también la conexión inversa (asumimos grafo no dirigido)

    def mover_agente(self, nodo):
        self.posicion_actual = nodo  #Actualiza la posición actual del agente
        self.explorado.add(nodo)  #Marca el nodo como explorado

    def observar_vecinos(self, nodo):
        return self.mapa_real[nodo]  #Devuelve los vecinos del nodo actual, simulando la observación en línea

def busqueda_online(entorno, inicio, objetivo):
    frontera = deque([inicio])  #Cola para la búsqueda BFS en línea
    camino = {inicio: None}  #Diccionario para rastrear el camino

    entorno.mover_agente(inicio)  #El agente se posiciona en el nodo inicial

    while frontera:
        actual = frontera.popleft()  #Toma el siguiente nodo de la frontera
        entorno.mover_agente(actual)  #Se mueve al nodo actual

        if actual == objetivo:  #Si alcanza el objetivo
            #Reconstruir camino
            ruta = []
            while actual:
                ruta.append(actual)
                actual = camino[actual]
            return ruta[::-1]  #Devuelve el camino desde el inicio hasta el objetivo

        for vecino in entorno.observar_vecinos(actual):  #Descubre los vecinos del nodo actual
            if vecino not in camino:  #Si el vecino no ha sido registrado aún
                camino[vecino] = actual  #Registra de dónde vino para poder reconstruir la ruta
                frontera.append(vecino)  #Agrega el vecino a la frontera

    return None  #Si no encuentra el objetivo

#Prueba del algoritmo
entorno = EntornoDesconocido()
entorno.agregar_arista("A", "B")
entorno.agregar_arista("A", "C")
entorno.agregar_arista("B", "D")
entorno.agregar_arista("C", "E")
entorno.agregar_arista("D", "F")
entorno.agregar_arista("E", "F")
entorno.agregar_arista("F", "G")

ruta = busqueda_online(entorno, "A", "G")  #Inicia la búsqueda desde A hacia G

if ruta:
    print(f"Ruta encontrada por el agente online: {' -> '.join(ruta)}")  #Imprime el camino encontrado
else:
    print("No se encontró una ruta al objetivo.")  #Informa si no se halló solución