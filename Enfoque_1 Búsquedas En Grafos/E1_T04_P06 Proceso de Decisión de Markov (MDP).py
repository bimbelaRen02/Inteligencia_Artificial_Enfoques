"""Utilidad y Toma de Decisiones - Proceso de Decisión de Markov (MDP).
Un Proceso de Decisión de Markov (MDP) modela entornos de decisión secuencial donde los resultados son inciertos,
pero están gobernados por probabilidades conocidas. Está compuesto por estados, acciones, recompensas y transiciones probabilísticas."""

#Estados del entorno
estados = ['S1', 'S2', 'S3']

#Acciones disponibles por estado
acciones = {
    'S1': ['a1', 'a2'],
    'S2': ['a1', 'a2'],
    'S3': []  #Estado terminal
}

#Transiciones probabilísticas: (estado, acción) -> [(estado_siguiente, probabilidad)]
transiciones = {
    ('S1', 'a1'): [('S1', 0.5), ('S2', 0.5)],
    ('S1', 'a2'): [('S2', 1.0)],
    ('S2', 'a1'): [('S3', 1.0)],
    ('S2', 'a2'): [('S1', 0.5), ('S3', 0.5)]
}

#Recompensas por llegar a un estado
recompensas = {
    'S1': 0,
    'S2': 5,
    'S3': 10  #Estado objetivo con máxima utilidad
}

#Parámetros del MDP
gamma = 0.9  #Factor de descuento
theta = 0.01  #Umbral de convergencia

#Inicialización de valores de los estados
V = {estado: 0 for estado in estados}

#Algoritmo de Iteración de Valores para resolver el MDP
def iteracion_de_valores():
    while True:
        delta = 0
        for s in estados:
            if not acciones[s]:  #Si es estado terminal, no se evalúa
                continue
            v = V[s]
            max_valor = float('-inf')
            for a in acciones[s]:
                total = 0
                for (siguiente, prob) in transiciones.get((s, a), []):
                    total += prob * (recompensas[siguiente] + gamma * V[siguiente])
                max_valor = max(max_valor, total)  #Selecciona la mejor acción
            V[s] = max_valor
            delta = max(delta, abs(v - V[s]))
        if delta < theta:  #Convergencia alcanzada
            break

#Política derivada de los valores
def derivar_politica():
    politica = {}
    for s in estados:
        if not acciones[s]:
            politica[s] = 'terminal'
            continue
        mejor_accion = None
        mejor_valor = float('-inf')
        for a in acciones[s]:
            total = 0
            for (siguiente, prob) in transiciones.get((s, a), []):
                total += prob * (recompensas[siguiente] + gamma * V[siguiente])
            if total > mejor_valor:
                mejor_valor = total
                mejor_accion = a
        politica[s] = mejor_accion
    return politica

#Ejecutamos el algoritmo
iteracion_de_valores()
politica_optima = derivar_politica()

#Mostramos resultados
print("Valores óptimos de cada estado:")
for estado in estados:
    print(f"{estado}: {V[estado]:.3f}")

print("\nPolítica óptima derivada:")
for estado, accion in politica_optima.items():
    print(f"{estado}: acción -> {accion}")