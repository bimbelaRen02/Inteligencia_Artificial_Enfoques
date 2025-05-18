"""Utilidad y Toma de Decisiones - Red Bayesiana Dinámica.
Una Red Bayesiana Dinámica (DBN) modela procesos estocásticos que evolucionan en el tiempo mediante una serie de redes bayesianas conectadas secuencialmente,
permitiendo representar cómo las variables cambian y se influyen entre sí en diferentes pasos temporales."""

import random

#Estados posibles de una variable en el tiempo
estados_clima = ['Soleado', 'Lluvioso']
estados_actividad = ['Salir', 'Quedarse']

#Distribución inicial de clima en t=0
prior_clima = {'Soleado': 0.7, 'Lluvioso': 0.3}

#Probabilidad de transición del clima: P(Clima_t | Clima_t-1)
transicion_clima = {
    'Soleado': {'Soleado': 0.8, 'Lluvioso': 0.2},
    'Lluvioso': {'Soleado': 0.4, 'Lluvioso': 0.6}
}

#Probabilidad condicional de actividad según clima: P(Actividad_t | Clima_t)
prob_actividad_dada_clima = {
    'Soleado': {'Salir': 0.9, 'Quedarse': 0.1},
    'Lluvioso': {'Salir': 0.2, 'Quedarse': 0.8}
}

#Función para muestrear un valor a partir de una distribución
def muestrear(distribucion):
    return random.choices(list(distribucion.keys()), weights=list(distribucion.values()))[0]

#Simulación de una Red Bayesiana Dinámica por varios pasos de tiempo
def simular_dinamica(tiempo_total):
    clima_actual = muestrear(prior_clima)  #Primer estado del clima
    historia = []

    for t in range(tiempo_total):
        actividad = muestrear(prob_actividad_dada_clima[clima_actual])  #Actividad según el clima actual
        historia.append((t, clima_actual, actividad))
        clima_actual = muestrear(transicion_clima[clima_actual])  #Transición de clima para siguiente t

    return historia

#Ejecutamos la simulación por 5 pasos de tiempo
historial = simular_dinamica(5)
print("Simulación de Red Bayesiana Dinámica (Clima vs Actividad):\n")
for t, clima, actividad in historial:
    print(f"t={t}: Clima = {clima}, Actividad = {actividad}")