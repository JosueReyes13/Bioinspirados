"""Este código basado en un enjambre es un metodo de optimización
el cual copia y simula el comportamiento social de las bandadas de aves, 
bancos de peces, etc."""

import random

# Esta función de esfera devuelve la aptitud que se desea optimizar
def aptitud(x):
    return sum([xi**2 for xi in x])

# Inicializar las partículas
def inicializar_particulas(num_particulas, dimensiones, rango):
    particulas = []
    for _ in range(num_particulas):
        particula = [random.uniform(rango[0], rango[1]) for _ in range(dimensiones)]
        particulas.append(particula)
    return particulas

# Inicializar las velocidades
def inicializar_velocidades(num_particulas, dimensiones, rango):
    velocidades = []
    for _ in range(num_particulas):
        velocidad = [random.uniform(-abs(rango[1] - rango[0]), abs(rango[1] - rango[0])) for _ in range(dimensiones)]
        velocidades.append(velocidad)
    return velocidades

# PSO
""" Aqui se ajustan las velocidades y posiciones de las particulas para 
minimizar la aptitud"""
def pso(num_particulas, dimensiones, rango, iteraciones, w=0.5, c1=1.5, c2=1.5):
    # Inicializar partículas y velocidades
    particulas = inicializar_particulas(num_particulas, dimensiones, rango)
    velocidades = inicializar_velocidades(num_particulas, dimensiones, rango)

    # Inicializar la mejor posición global y la mejor posición de cada partícula
    mejores_posiciones = particulas[:]
    mejores_aptitudes = [aptitud(p) for p in particulas]
    mejor_global = particulas[mejores_aptitudes.index(min(mejores_aptitudes))]

    for _ in range(iteraciones):
        for i in range(num_particulas):
            # Actualizar la velocidad de cada partícula
            for d in range(dimensiones):
                r1, r2 = random.random(), random.random()
                velocidades[i][d] = (w * velocidades[i][d] +
                                     c1 * r1 * (mejores_posiciones[i][d] - particulas[i][d]) +
                                     c2 * r2 * (mejor_global[d] - particulas[i][d]))

            # Actualizar la posición de cada partícula
            particulas[i] = [particulas[i][d] + velocidades[i][d] for d in range(dimensiones)]

            # Evaluar la nueva posición
            aptitud_actual = aptitud(particulas[i])

            # Actualizar la mejor posición personal
            if aptitud_actual < mejores_aptitudes[i]:
                mejores_aptitudes[i] = aptitud_actual
                mejores_posiciones[i] = particulas[i]

        # Actualizar la mejor posición global
        mejor_global = mejores_posiciones[mejores_aptitudes.index(min(mejores_aptitudes))]

    return mejor_global, min(mejores_aptitudes)

# Parámetros del PSO
"""Aqui se ejecuta el algoritmo con los parametros definidos y se da
la mejor solución y su aptitud"""
num_particulas = 30
dimensiones = 2
rango = (-10, 10)
iteraciones = 100

# Ejecutar PSO
mejor_solucion, mejor_aptitud = pso(num_particulas, dimensiones, rango, iteraciones)

print("Mejor solución:", mejor_solucion)
print("Mejor aptitud:", mejor_aptitud)
