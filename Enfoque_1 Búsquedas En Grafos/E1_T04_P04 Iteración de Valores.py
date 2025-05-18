"""Utilidad y Toma de Decisiones - Iteración de Valores.
La Iteración de Valores es un algoritmo de programación dinámica utilizado en procesos de decisión de Markov (MDP)
para encontrar la política óptima al actualizar repetidamente los valores esperados de los estados hasta la convergencia."""

#Estados posibles del entorno
estados = ['A', 'B', 'C', 'D', 'E']

#Acciones posibles en cada estado
acciones = ['izquierda', 'derecha']

#Modelo de transición: (estado_actual, acción) -> [(estado_siguiente, probabilidad)]
transiciones = {
    ('A', 'derecha'): [('B', 1.0)],
    ('B', 'izquierda'): [('A', 1.0)],
    ('B', 'derecha'): [('C', 1.0)],
    ('C', 'izquierda'): [('B', 1.0)],
    ('C', 'derecha'): [('D', 1.0)],
    ('D', 'izquierda'): [('C', 1.0)],
    ('D', 'derecha'): [('E', 1.0)],
    ('E', 'izquierda'): [('D', 1.0)]
}

#Recompensas inmediatas por estar en un estado
recompensas = {
    'A': 0,
    'B': 0,
    'C': -1,
    'D': 0,
    'E': 10  #Estado objetivo
}

#Parámetros
gamma = 0.9  #Factor de descuento
theta = 0.001  #Umbral de convergencia

#Inicializamos valores de los estados en 0
V = {estado: 0 for estado in estados}

#Iteración de valores
def iteracion_de_valores():
    while True:
        delta = 0
        for s in estados:
            if s not in recompensas:
                continue
            v = V[s]
            max_valor = float('-inf')
            for a in acciones:
                if (s, a) in transiciones:
                    total = 0
                    for (siguiente, prob) in transiciones[(s, a)]:
                        total += prob * (recompensas[siguiente] + gamma * V[siguiente])  #Ecuación de Bellman
                    max_valor = max(max_valor, total)
            if max_valor != float('-inf'):
                V[s] = max_valor
                delta = max(delta, abs(v - V[s]))
        if delta < theta:  #Criterio de convergencia
            break

#Ejecutamos la iteración
iteracion_de_valores()

#Mostramos los valores óptimos de cada estado
print("Valores óptimos de los estados después de la Iteración de Valores:")
for estado in estados:
    print(f"Estado {estado}: Valor = {V[estado]:.3f}")