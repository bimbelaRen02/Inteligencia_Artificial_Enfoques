"""Utilidad y Toma de Decisiones - Iteración de Políticas.
La Iteración de Políticas es un algoritmo de optimización en procesos de decisión de Markov (MDP),
que alterna entre evaluar una política y mejorarla, hasta encontrar una política óptima."""

#Estados posibles del entorno
estados = ['A', 'B', 'C', 'D', 'E']

#Acciones posibles en cada estado
acciones = ['izquierda', 'derecha']

#Modelo de transición: (estado, acción) -> [(estado_siguiente, probabilidad)]
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

#Inicialización de valores y política arbitraria
V = {estado: 0 for estado in estados}
politica = {estado: 'derecha' for estado in estados if estado != 'E'}

#Evaluación de la política actual
def evaluar_politica():
    while True:
        delta = 0
        for s in estados:
            if s not in politica:
                continue
            v = V[s]
            a = politica[s]
            total = 0
            if (s, a) in transiciones:
                for (siguiente, prob) in transiciones[(s, a)]:
                    total += prob * (recompensas[siguiente] + gamma * V[siguiente])  #Ecuación de Bellman para política fija
            V[s] = total
            delta = max(delta, abs(v - V[s]))
        if delta < theta:  #Criterio de convergencia
            break

#Mejora de la política actual
def mejorar_politica():
    estable = True
    for s in estados:
        if s not in politica:
            continue
        mejor_accion = politica[s]
        mejor_valor = V[s]
        for a in acciones:
            if (s, a) in transiciones:
                total = 0
                for (siguiente, prob) in transiciones[(s, a)]:
                    total += prob * (recompensas[siguiente] + gamma * V[siguiente])
                if total > mejor_valor:
                    mejor_valor = total
                    mejor_accion = a
        if mejor_accion != politica[s]:
            politica[s] = mejor_accion
            estable = False
    return estable

#Iteración principal: evaluar y mejorar hasta convergencia
def iteracion_de_politicas():
    while True:
        evaluar_politica()
        if mejorar_politica():  #Si no hubo cambios, la política es óptima
            break

#Ejecutamos la Iteración de Políticas
iteracion_de_politicas()

#Mostramos la política óptima y valores
print("Política óptima después de la Iteración de Políticas:")
for estado in estados:
    accion = politica.get(estado, 'Ninguna')
    print(f"Estado {estado}: Acción = {accion}")

print("\nValores asociados a la política óptima:")
for estado in estados:
    print(f"Estado {estado}: Valor = {V[estado]:.3f}")