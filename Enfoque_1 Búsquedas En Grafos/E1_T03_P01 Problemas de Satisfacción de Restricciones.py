"""Planificación (3): Satisfacción De Restricciones - Problemas de Satisfacción de Restricciones.
Los Problemas de Satisfacción de Restricciones (CSP) consisten en encontrar valores para un conjunto
de variables que cumplan con ciertas restricciones. Son comunes en horarios, mapas, sudoku,
criptogramas y otros problemas de lógica."""

def es_valido(asignacion, variable, valor, restricciones):
    for (var1, var2) in restricciones:
        if var1 == variable:
            if var2 in asignacion and not restricciones[(var1, var2)](valor, asignacion[var2]):
                return False  #Si al aplicar la restricción con otra variable ya asignada no se cumple, no es válido
        elif var2 == variable:
            if var1 in asignacion and not restricciones[(var1, var2)](asignacion[var1], valor):
                return False  #Evalúa simétricamente si se cumple la restricción del otro lado
    return True  #Si todas las restricciones se cumplen, es válido

def backtracking(asignacion, variables, dominios, restricciones): #Se define backtraking que funciona como un algoritmo de búsqueda
    if len(asignacion) == len(variables):  #Si ya se asignaron todas las variables
        return asignacion  #Se ha encontrado una solución completa

    variable = next(v for v in variables if v not in asignacion)  #Selecciona la siguiente variable sin asignar

    for valor in dominios[variable]:
        if es_valido(asignacion, variable, valor, restricciones):  #Si el valor no viola restricciones
            asignacion[variable] = valor  #Asigna el valor
            resultado = backtracking(asignacion, variables, dominios, restricciones)  #Busca recursivamente
            if resultado:
                return resultado  #Si se encontró una solución, la devuelve
            del asignacion[variable]  #Si no, deshace la asignación (backtracking)

    return None  #Si ningún valor funcionó, regresa None

#Prueba del algoritmo: Mapa de 3 regiones con restricciones de colores distintos (estilo problema de mapas)
variables = ["A", "B", "C"]  #Regiones
dominios = {
    "A": ["rojo", "verde", "azul"],
    "B": ["rojo", "verde", "azul"],
    "C": ["rojo", "verde", "azul"]
}

#Restricciones binarias: las regiones adyacentes no deben tener el mismo color
restricciones = {
    ("A", "B"): lambda a, b: a != b,
    ("B", "C"): lambda a, b: a != b,
    ("A", "C"): lambda a, b: a != b
}

solucion = backtracking({}, variables, dominios, restricciones) #Backtracking se encarga de encontrar la solución al CSP

#Prueba del algoritmo
if solucion:
    print("Solución encontrada para el CSP:")
    for var in sorted(solucion):
        print(f"{var}: {solucion[var]}")  #Muestra cada región con su color
else:
    print("No se encontró una solución para el CSP.")