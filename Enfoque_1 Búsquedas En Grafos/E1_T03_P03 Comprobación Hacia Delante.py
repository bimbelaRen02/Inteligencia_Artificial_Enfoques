"""Planificación (3): Satisfacción De Restricciones - Comprobación Hacia Delante.
Forward Checking reduce los dominios de las variables no asignadas conforme se realizan
asignaciones, eliminando valores inconsistentes para evitar conflictos futuros."""

def es_valido_fc(variable, valor, asignacion, restricciones):
    for (var1, var2) in restricciones:
        if var1 == variable and var2 in asignacion:
            if not restricciones[(var1, var2)](valor, asignacion[var2]):
                return False  #Si la asignación del valor rompe una restricción con una variable ya asignada
        elif var2 == variable and var1 in asignacion:
            if not restricciones[(var1, var2)](asignacion[var1], valor):
                return False  #Evalúa la restricción en la otra dirección
    return True  #Si no hay conflictos, es válido

def forward_checking(variable, valor, dominios, asignacion, restricciones):
    dominios_filtrados = {var: list(dom) for var, dom in dominios.items()}  #Copia profunda de los dominios
    for (var1, var2) in restricciones:
        vecino = None
        if var1 == variable:
            vecino = var2
        elif var2 == variable:
            vecino = var1

        if vecino and vecino not in asignacion:
            nuevos_valores = []
            for v in dominios_filtrados[vecino]:
                if var1 == variable:
                    if restricciones[(var1, var2)](valor, v):
                        nuevos_valores.append(v)
                else:
                    if restricciones[(var1, var2)](v, valor):
                        nuevos_valores.append(v)

            if not nuevos_valores:
                return None  #Si se elimina todo el dominio de una variable futura, hay que retroceder
            dominios_filtrados[vecino] = nuevos_valores  #Actualiza el dominio filtrado
    return dominios_filtrados  #Devuelve dominios reducidos si todo está bien

def comprobar_adelante(asignacion, variables, dominios, restricciones):
    if len(asignacion) == len(variables):  #Si ya se asignaron todas las variables
        return asignacion  #Se encontró una solución

    variable = next(v for v in variables if v not in asignacion)  #Elige la siguiente variable no asignada

    for valor in dominios[variable]:
        if es_valido_fc(variable, valor, asignacion, restricciones):  #Verifica que el valor no viole restricciones
            asignacion[variable] = valor  #Asigna provisionalmente
            nuevos_dominios = forward_checking(variable, valor, dominios, asignacion, restricciones)  #Filtra dominios
            if nuevos_dominios:
                resultado = comprobar_adelante(asignacion, variables, nuevos_dominios, restricciones)  #Llama recursiva
                if resultado:
                    return resultado  #Si la llamada recursiva tuvo éxito, devuelve resultado
            del asignacion[variable]  #Retrocede si no hubo solución posible
    return None  #No se encontró una solución con esta configuración

#Prueba del algoritmo: mismo problema del mapa de 3 regiones
variables = ["X", "Y", "Z"]
dominios = {
    "X": ["rojo", "verde", "azul"],
    "Y": ["rojo", "verde", "azul"],
    "Z": ["rojo", "verde", "azul"]
}
restricciones = {
    ("X", "Y"): lambda a, b: a != b,
    ("Y", "Z"): lambda a, b: a != b,
    ("X", "Z"): lambda a, b: a != b
}

solucion = comprobar_adelante({}, variables, dominios, restricciones)

#Prueba del algoritmo
if solucion:
    print("Solución encontrada con Comprobación Hacia Delante:")
    for var in sorted(solucion):
        print(f"{var}: {solucion[var]}")
else:
    print("No se encontró solución.")