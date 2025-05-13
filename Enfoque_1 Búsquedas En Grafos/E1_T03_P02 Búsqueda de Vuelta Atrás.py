"""Planificación (3): Satisfacción De Restricciones - Búsqueda de Vuelta Atrás.
La búsqueda de vuelta atrás (backtracking) es una técnica sistemática para
resolver CSPs al asignar valores a variables de forma incremental y retroceder
cuando se encuentra una violación de restricciones."""

def es_valido(asignacion, variable, valor, restricciones):
    for (var1, var2) in restricciones:
        if var1 == variable and var2 in asignacion and not restricciones[(var1, var2)](valor, asignacion[var2]):
            return False  #Si al evaluar la restricción con una variable ya asignada no se cumple, es inválido
        elif var2 == variable and var1 in asignacion and not restricciones[(var1, var2)](asignacion[var1], valor):
            return False  #Evalúa simétricamente la otra dirección de la restricción
    return True  #Si todas las restricciones se cumplen, el valor es válido

def vuelta_atras(asignacion, variables, dominios, restricciones):
    if len(asignacion) == len(variables):  #Si ya se han asignado todas las variables
        return asignacion  #Devuelve la solución completa

    variable = next(v for v in variables if v not in asignacion)  #Selecciona la siguiente variable sin asignar

    for valor in dominios[variable]:
        if es_valido(asignacion, variable, valor, restricciones):  #Verifica si el valor cumple restricciones
            asignacion[variable] = valor  #Asigna provisionalmente el valor
            resultado = vuelta_atras(asignacion, variables, dominios, restricciones)  #Llama recursivamente
            if resultado:
                return resultado  #Si se encontró solución, la retorna
            print(f"Retrocediendo... quitando asignación {variable} = {valor}")  #Indica retroceso
            del asignacion[variable]  #Retrocede (backtrack) si no funcionó

    return None  #No se encontró una solución válida con la configuración actual

#Prueba del algoritmo: problema de asignación de colores en un mapa simple
variables = ["X", "Y", "Z"]  #Tres regiones o nodos
dominios = {
    "X": ["rojo", "verde", "azul"],
    "Y": ["rojo", "verde", "azul"],
    "Z": ["rojo", "verde", "azul"]
}

#Restricciones: ninguna región adyacente debe tener el mismo color
restricciones = {
    ("X", "Y"): lambda a, b: a != b,
    ("Y", "Z"): lambda a, b: a != b,
    ("X", "Z"): lambda a, b: a != b
}

solucion = vuelta_atras({}, variables, dominios, restricciones)

#Prueba del algoritmo
if solucion:
    print("Solución encontrada con Búsqueda de Vuelta Atrás:")
    for var in sorted(solucion):
        print(f"{var}: {solucion[var]}")  #Muestra cada variable con su valor asignado
else:
    print("No se encontró solución.")