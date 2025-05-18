"""Utilidad y Toma de Decisiones - Teoría de la Utilidad: Función de Utilidad
La teoría de la utilidad permite que un agente racional seleccione la mejor acción bajo incertidumbre,
asignando valores numéricos (utilidades) a los posibles resultados. La acción óptima será la que maximice
la utilidad esperada, calculada como la suma ponderada de las utilidades según sus probabilidades."""

#Definimos la utilidad de cada posible resultado
utilidad = {
    'éxito_alto': 100,     #Resultado altamente deseado
    'éxito_medio': 70,     #Resultado moderadamente deseado
    'éxito_bajo': 40,      #Resultado aceptable
    'fracaso': 0           #Resultado no deseado
}

#Definimos las acciones posibles y las probabilidades de sus resultados
acciones = {
    'arriesgar': {
        'éxito_alto': 0.4,    #Probabilidad de éxito alto
        'éxito_medio': 0.2,   #Probabilidad de éxito medio
        'fracaso': 0.4        #Probabilidad de fracaso
    },
    'conservador': {
        'éxito_medio': 0.6,   #Alta probabilidad de éxito medio
        'éxito_bajo': 0.3,    #Probabilidad de éxito bajo
        'fracaso': 0.1        #Baja probabilidad de fracaso
    }
}

#Función para calcular la utilidad esperada de una acción
def utilidad_esperada(accion):
    total = 0  #Inicializa acumulador
    for resultado, probabilidad in acciones[accion].items():
        u = utilidad.get(resultado, 0)  #Obtiene utilidad del resultado
        total += probabilidad * u  #Suma ponderada por probabilidad
    return total  #Devuelve la utilidad esperada total

#Mostrar utilidad esperada de cada acción
for accion in acciones:
    ue = utilidad_esperada(accion)
    print(f"Utilidad esperada de '{accion}': {ue}")  #Imprime utilidad esperada

#Seleccionar la mejor acción según la utilidad esperada
mejor_accion = max(acciones, key=utilidad_esperada)  #Encuentra la de mayor utilidad
print(f"\nAcción recomendada: '{mejor_accion}'")  #Muestra decisión óptima
