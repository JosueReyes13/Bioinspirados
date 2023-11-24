"""El rococido simulado es un algoritmo de optimizaciónel cual
se usa para encontrar soluciones aproximadas a problemas de 
optimización combinatoria y continua, esta inspirado en el 
proceso metalúrgico llamado "recocido" en el que un material
se calienta y luego se enfria lentamente para eliminar defectos
y mejorar su estructura cristalina"""

import random
import math

"""Definimos la función "distancia" la cual calcula la 
distancia euclidiana entre dos ciudades espetando como pares
de coordenadas (x,y)"""
def distancia(ciudad1, ciudad2):
    return math.sqrt((ciudad1[0] - ciudad2[0])**2 + (ciudad1[1] - ciudad2[1])**2)

"""Esta funciónse encarga de calcular la longitud de una ruta
dada una secuencia de ciudades y sus coordenadas, utiliza la 
función de arriba (distancia) para calcular la distancia entre 
las ciudades en la ruta"""
def longitud_ruta(ruta, ciudades):
    distancia_total = 0
    for i in range(len(ruta) - 1):
        distancia_total += distancia(ciudades[ruta[i]], ciudades[ruta[i+1]])
    distancia_total += distancia(ciudades[ruta[-1]], ciudades[ruta[0]])
    return distancia_total

"""Aqui es donde el recocido simulado se lleva a cabo, aqui
se ejecuta dentro de un bucle que realiza un numero especifico 
de iteraciones, cada iteración tiene como objetivomejorar la ruta
actual explorando rutas vecinas y potencialmente aceptando 
rutas que sean peores que la actual con una cierta probabilidad"""
# Función de recocido simulado.
def recocido_simulado(ciudades, temperatura_inicial, factor_enfriamiento, iteraciones):
    n = len(ciudades)
    ruta_actual = random.sample(range(n), n)  # Generar una ruta inicial aleatoria
    temperatura = temperatura_inicial
    
    for i in range(iteraciones):
        # Generar una ruta vecina intercambiando dos ciudades aleatorias.
        ruta_vecina = ruta_actual[:]
        i, j = random.sample(range(n), 2)
        ruta_vecina[i], ruta_vecina[j] = ruta_vecina[j], ruta_vecina[i]
        
        # Calcular la diferencia en la longitud de las rutas.
        delta_distancia = longitud_ruta(ruta_vecina, ciudades) - longitud_ruta(ruta_actual, ciudades)
        
        # Si la nueva ruta es más corta o se acepta de acuerdo con la temperatura, actualiza la ruta actual.
        if delta_distancia < 0 or random.random() < math.exp(-delta_distancia / temperatura):
            ruta_actual = ruta_vecina
        
        # Reduce la temperatura.
        temperatura *= factor_enfriamiento
    
    return ruta_actual, longitud_ruta(ruta_actual, ciudades)

"""Como ejemplo de uso, creamos una lista de coordenadas de
ciudades, la temperatura inicial, el factor de enfriamiento
y el número de iteraciones, luego ejecutamos el código y 
mostramos la ruta y su longitud"""
ciudades = [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]
temperatura_inicial = 1000
factor_enfriamiento = 0.98
iteraciones = 1000

ruta_optima, longitud_optima = recocido_simulado(ciudades, temperatura_inicial, factor_enfriamiento, iteraciones)
print("Ruta óptima:", ruta_optima)
print("Longitud óptima:", longitud_optima)
