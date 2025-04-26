"""Planificación (2): Búsqueda Informada - Algoritmos Genéticos.
Los Algoritmos Genéticos (AG) son una técnica de búsqueda inspirada en la evolución natural. Usan mecanismos como la selección, el cruce y la mutación para encontrar soluciones 
a problemas complejos. Son especialmente útiles cuando no se puede utilizar una búsqueda exhaustiva debido al gran tamaño del espacio de soluciones."""

import random

#Función de aptitud (fitness): Calcula la similitud entre un individuo y el objetivo
def fitness(individuo, objetivo):
    return sum([1 for i, j in zip(individuo, objetivo) if i == j])  #Cuenta cuántos genes del individuo coinciden con el objetivo

#Cruzamiento (crossover): Combina dos individuos para generar dos nuevos
def cruce(padre1, padre2):
    punto_cruce = random.randint(1, len(padre1)-1)  #Selecciona un punto aleatorio donde se realizará el cruce entre los dos padres
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]  #El hijo 1 toma los genes del padre 1 hasta el punto de cruce y los genes del padre 2 después del punto de cruce
    hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]  #El hijo 2 toma los genes del padre 2 hasta el punto de cruce y los genes del padre 1 después del punto de cruce
    return hijo1, hijo2  #Devuelve los dos hijos generados

#Mutación: Modifica un individuo aleatoriamente con una cierta probabilidad
def mutacion(individuo, prob_mutacion):
    if random.random() < prob_mutacion:  #Decide aleatoriamente si realizar la mutación según la probabilidad dada
        i = random.randint(0, len(individuo)-1)  #Selecciona un índice aleatorio del individuo para modificarlo
        nuevo_gen = random.choice("01")  #Selecciona un nuevo gen aleatorio (en este caso, '0' o '1')
        individuo = individuo[:i] + nuevo_gen + individuo[i+1:]  #Cambia el gen en la posición seleccionada por el nuevo gen
    return individuo  #Devuelve el individuo mutado

#Selección por torneo: Elige el mejor individuo entre un grupo seleccionado aleatoriamente
def seleccion_torneo(poblacion, objetivo):
    torneo = random.sample(poblacion, 3)  #Selecciona aleatoriamente 3 individuos de la población para competir
    torneo = sorted(torneo, key=lambda x: fitness(x, objetivo), reverse=True)  #Ordena los individuos seleccionados según su aptitud (mayor aptitud primero)
    return torneo[0]  #Devuelve el individuo con la mayor aptitud (el mejor del torneo)

#Algoritmo Genético
def algoritmo_genetico(objetivo, tam_poblacion=100, prob_mutacion=0.01, max_generaciones=100):
    poblacion = [''.join(random.choices("01", k=len(objetivo))) for _ in range(tam_poblacion)]  #Genera una población inicial de individuos aleatorios con la longitud del objetivo

    for generacion in range(max_generaciones):  #Itera a través de un número máximo de generaciones
        nueva_poblacion = []  #Lista para almacenar la nueva población generada

        while len(nueva_poblacion) < tam_poblacion:  #Crea nuevos individuos hasta llenar la población
            padre1 = seleccion_torneo(poblacion, objetivo)  #Selecciona el primer padre
            padre2 = seleccion_torneo(poblacion, objetivo)  #Selecciona el segundo padre
            hijo1, hijo2 = cruce(padre1, padre2)  #Realiza el cruce entre los dos padres
            nueva_poblacion.append(mutacion(hijo1, prob_mutacion))  #Aplica mutación al hijo 1 y lo agrega a la nueva población
            if len(nueva_poblacion) < tam_poblacion:  #Si la nueva población no está llena, agrega el segundo hijo
                nueva_poblacion.append(mutacion(hijo2, prob_mutacion))  #Aplica mutación al hijo 2 y lo agrega a la nueva población

        poblacion = nueva_poblacion  #Actualiza la población con la nueva población generada

        for individuo in poblacion:  #Comprobamos si alguna solución es igual al objetivo
            if fitness(individuo, objetivo) == len(objetivo):  #Si encontramos una solución que coincide con el objetivo, devolvemos el individuo y la generación
                return individuo, generacion  

    return None, max_generaciones  #Si no se encuentra solución, devolvemos None y el número máximo de generaciones

#Prueba del algoritmo
objetivo = "1010101010101010"  #Define el objetivo
solucion, generaciones = algoritmo_genetico(objetivo)  #Llama al algoritmo genético con el objetivo

if solucion:  #Si se encuentra una solución
    print(f"Solución encontrada: {solucion} en {generaciones} generaciones.")  #Imprime la solución y el número de generaciones
else:
    print(f"No se encontró solución en {generaciones} generaciones.")  #Si no se encuentra solución, informa cuántas generaciones se intentaron