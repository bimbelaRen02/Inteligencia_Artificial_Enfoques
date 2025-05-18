"""Utilidad y Toma de Decisiones - MDP Parcialmente Observable (POMDP).
Un MDP Parcialmente Observable (POMDP) extiende al MDP al considerar que el agente no conoce con certeza el estado actual,
sino que mantiene una creencia (distribución de probabilidad) sobre los posibles estados y actualiza esta creencia mediante observaciones."""

import random

#Estados posibles
estados = ['Sano', 'Enfermo']

#Acciones disponibles
acciones = ['Esperar', 'Tratar']

#Observaciones posibles
observaciones = ['Bien', 'Mal']

#Probabilidad de observación dada un estado
prob_obs = {
    'Sano': {'Bien': 0.8, 'Mal': 0.2},
    'Enfermo': {'Bien': 0.3, 'Mal': 0.7}
}

#Modelo de transición: (estado, acción) -> {estado_siguiente: probabilidad}
transiciones = {
    ('Sano', 'Esperar'): {'Sano': 0.9, 'Enfermo': 0.1},
    ('Sano', 'Tratar'): {'Sano': 1.0},
    ('Enfermo', 'Esperar'): {'Enfermo': 0.8, 'Sano': 0.2},
    ('Enfermo', 'Tratar'): {'Sano': 0.6, 'Enfermo': 0.4}
}

#Recompensas: (estado, acción)
recompensas = {
    ('Sano', 'Esperar'): 5,
    ('Sano', 'Tratar'): 1,
    ('Enfermo', 'Esperar'): -1,
    ('Enfermo', 'Tratar'): 3
}

#Belief inicial (creencia sobre el estado actual)
creencia = {'Sano': 0.5, 'Enfermo': 0.5}

#Función para actualizar la creencia usando el teorema de Bayes
def actualizar_creencia(creencia, accion, observacion):
    nueva_creencia = {}
    for s_prime in estados:
        total = 0
        for s in estados:
            trans = transiciones.get((s, accion), {})
            total += creencia[s] * trans.get(s_prime, 0)
        obs_prob = prob_obs[s_prime][observacion]
        nueva_creencia[s_prime] = obs_prob * total
    normalizador = sum(nueva_creencia.values())
    for s in estados:
        nueva_creencia[s] /= normalizador  #Normalización
    return nueva_creencia

#Función para seleccionar acción basada en utilidad esperada (greedy)
def seleccionar_mejor_accion(creencia):
    mejor_accion = None
    mejor_utilidad = float('-inf')
    for a in acciones:
        utilidad = 0
        for s in estados:
            utilidad += creencia[s] * recompensas[(s, a)]
        if utilidad > mejor_utilidad:
            mejor_utilidad = utilidad
            mejor_accion = a
    return mejor_accion

#Simulación de un paso en POMDP
def paso_pomdp(creencia):
    accion = seleccionar_mejor_accion(creencia)
    print(f"Acción seleccionada: {accion}")

    #Simulamos el estado real oculto
    estado_real = random.choices(estados, weights=[creencia[s] for s in estados])[0]

    #Simulamos la transición del estado real
    siguiente_estado = random.choices(estados, weights=list(transiciones[(estado_real, accion)].values()))[0]

    #Generamos una observación basada en el nuevo estado
    observacion = random.choices(observaciones, weights=list(prob_obs[siguiente_estado].values()))[0]
    print(f"Observación recibida: {observacion}")

    #Actualizamos la creencia
    nueva_creencia = actualizar_creencia(creencia, accion, observacion)
    print(f"Nueva creencia: {nueva_creencia}")
    return nueva_creencia

#Ejemplo de ejecución de 5 pasos
print("POMDP - Simulación de pasos:")
for paso in range(5):
    print(f"\nPaso {paso + 1}:")
    creencia = paso_pomdp(creencia)