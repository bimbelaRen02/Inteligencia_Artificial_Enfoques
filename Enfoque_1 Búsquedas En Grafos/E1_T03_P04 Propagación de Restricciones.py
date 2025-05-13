"""Planificación (3): Satisfacción De Restricciones - Propagación de Restricciones (AC-3).
AC-3 es un algoritmo que mantiene la consistencia arcial en un problema de satisfacción de
restricciones eliminando valores de los dominios que no cumplen con las restricciones binarias."""

from collections import deque

def ac3(variables, dominios, restricciones):
    cola = deque([(xi, xj) for (xi, xj) in restricciones])  #Cola de arcos a revisar

    while cola:
        xi, xj = cola.popleft()  #Toma un arco
        if revisar(xi, xj, dominios, restricciones):  #Revisa si se debe reducir el dominio de xi
            if not dominios[xi]:  #Si el dominio queda vacío, no hay solución posible
                return False
            for xk in vecinos(xi, xj, restricciones):  #Agrega arcos relacionados para revisar de nuevo
                cola.append((xk, xi))
    return True  #Todos los arcos fueron consistentes

def revisar(xi, xj, dominios, restricciones):
    revised = False
    for x in dominios[xi][:]:  #Itera sobre copia del dominio de xi
        if not any(restricciones[(xi, xj)](x, y) for y in dominios[xj]):  #Si no hay ningún valor de xj que cumpla
            dominios[xi].remove(x)  #Elimina x de dominio de xi
            revised = True  #Marca que hubo cambio
    return revised  #Retorna si hubo cambio en el dominio

def vecinos(xi, xj, restricciones):
    return [xk for (xk, xl) in restricciones if xl == xi and xk != xj]  #Busca vecinos diferentes a xj

#Prueba del algoritmo: mismo problema de colores
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

#Prueba del algoritmo
resultado = ac3(variables, dominios, restricciones)
if resultado:
    print("Dominio final tras aplicar AC-3:")
    for var in sorted(dominios):
        print(f"{var}: {dominios[var]}")
else:
    print("No se encontró solución (algún dominio quedó vacío).")