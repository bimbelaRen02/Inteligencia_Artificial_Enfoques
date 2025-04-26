"""Planificación (2): Búsqueda Informada - Heurísticas.
Las heurísticas son funciones que estiman el costo desde un estado actual hasta un objetivo, 
mejorando la eficiencia de los algoritmos de búsqueda al priorizar caminos prometedores."""

def heuristica(nodo, objetivo):
    return abs(ord(nodo) - ord(objetivo))  #Heurística basada en la distancia alfabética entre letras

#Prueba de la heurística
inicio = "A"
objetivo = "F"

estimacion = heuristica(inicio, objetivo)
print(f"Estimación heurística del nodo {inicio} al objetivo {objetivo}: {estimacion}")