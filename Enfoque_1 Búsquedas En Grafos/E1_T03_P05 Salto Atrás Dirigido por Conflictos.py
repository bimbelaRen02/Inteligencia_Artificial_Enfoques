"""Planificación (3): Satisfacción De Restricciones - Salto Atrás Dirigido por Conflictos.
El Salto Atrás Dirigido por Conflictos (CBJ) mejora la búsqueda de vuelta atrás
tradicional al saltar directamente hacia la fuente del conflicto en lugar de
retroceder paso a paso."""

def es_consistente(variable, valor, asignacion, restricciones):
    for otra_variable in asignacion:
        par1 = (variable, otra_variable)
        par2 = (otra_variable, variable)
        if par1 in restricciones and not restricciones[par1](valor, asignacion[otra_variable]):
            return False, otra_variable
        if par2 in restricciones and not restricciones[par2](asignacion[otra_variable], valor):
            return False, otra_variable
    return True, None

def cbj(variables, dominios, restricciones):
    asignacion = {}
    conflictos = {var: set() for var in variables}
    historial = []
    intento_maximo = 100
    intentos = 0

    historial.append((0, variables[0], dominios[variables[0]].copy(), asignacion.copy()))

    while historial and intentos < intento_maximo:
        i, variable, valores_restantes, asignacion = historial.pop()
        
        while valores_restantes:
            valor = valores_restantes.pop(0)
            consistente, culpable = es_consistente(variable, valor, asignacion, restricciones)

            if consistente:
                nueva_asignacion = asignacion.copy()
                nueva_asignacion[variable] = valor
                print(f"Variable {variable} = {valor}")
                
                if i + 1 == len(variables):
                    return nueva_asignacion
                
                siguiente_var = variables[i + 1]
                historial.append((i, variable, valores_restantes.copy(), asignacion.copy()))
                historial.append((i + 1, siguiente_var, dominios[siguiente_var].copy(), nueva_asignacion.copy()))
                break
            else:
                conflictos[variable].add(culpable)
                print(f"Conflicto: {variable}={valor} vs {culpable}={asignacion[culpable]}")

        else:
            if not conflictos[variable]:
                print(f"No solution for {variable}")
                return None
                
            ultima_conflictiva = max(conflictos[variable], key=lambda x: variables.index(x))
            nivel_conflicto = variables.index(ultima_conflictiva)
            
            # Propagate conflicts
            conflictos[ultima_conflictiva].update(conflictos[variable] - {ultima_conflictiva})
            conflictos[variable].clear()

            print(f"Backjumping to {ultima_conflictiva}")
            
            # Clear forward assignments
            for var in variables[nivel_conflicto+1:]:
                asignacion.pop(var, None)
                conflictos[var].clear()

            # Get remaining values for conflict variable
            dominio_original = dominios[variables[nivel_conflicto]].copy()
            valor_conflictivo = asignacion.get(variables[nivel_conflicto], None)
            valores_reintentar = [v for v in dominio_original if v != valor_conflictivo]
            
            if not valores_reintentar:
                print(f"No more values for {variables[nivel_conflicto]}")
                return None
                
            historial.append((nivel_conflicto, variables[nivel_conflicto], valores_reintentar, asignacion.copy()))
            intentos += 1

    print("Max attempts reached")
    return None

# Now with solvable domains (3 values for 3 variables)
variables = ["A", "B", "C"]
dominios = {
    "A": [1, 2, 3],
    "B": [1, 2, 3], 
    "C": [1, 2, 3]
}
restricciones = {
    ("A", "B"): lambda a, b: a != b,
    ("B", "C"): lambda b, c: b != c,
    ("A", "C"): lambda a, c: a != c
}

print("Running with solvable domains:")
solucion = cbj(variables, dominios, restricciones)
print("Solution:" if solucion else "No solution", solucion)