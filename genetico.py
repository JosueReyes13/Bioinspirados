import random

individuos = 30
los_bits = 1
el_rango = range(0, 15)

"""Esta función calcula la aptitud de un individuo"""
def calcular_aptitud(individuo):
    aptitud = sum([x**2 + 2 for x in individuo])
    return aptitud

"""Aqui se calcula la aptitud de todos los individuos y se elige el mejor"""
def most_apt(arreglo):
    apts = [calcular_aptitud(individuo) for individuo in arreglo]
    better_index = apts.index(max(apts))
    return arreglo[better_index], apts[better_index]

"""Aqui se cruza dos individuos """
def cruza(padre1, padre2):
    cross_point = random.randint(1, len(padre1))
    hijo1 = padre1[:cross_point] + padre2[cross_point:]
    hijo2 = padre2[:cross_point] + padre1[cross_point:]
    return hijo1, hijo2
"""Se crea a la población inicial"""
def mutacion(individuo, tasa_mutacion=0.01):
    for i in range(len(individuo)):
        if random.random() < tasa_mutacion:
            individuo[i] = random.choice(el_rango)
    return individuo

# Generar la población inicial
arreglo = [[random.choice(el_rango) for i in range(los_bits)] for i in range(individuos)]

# Representar la población en binario
el_binario = [[format(num, "04b") for num in individuo] for individuo in arreglo]
"""Selecciona 2 padres y se cruzan para generar 2 nuevos individuos
y estos van a reemplazar a los padres"""
print(el_binario)
print("\n")

# Evolucionar la población
generaciones = 10
tasa_mutacion = 0.01

for generacion in range(generaciones):
    print(f"Generación {generacion + 1}")
    
    # Seleccionar dos padres
    parent1_index = random.randint(0, individuos - 1)
    parent2_index = random.randint(0, individuos - 1)

    parent1 = arreglo[parent1_index]
    parent2 = arreglo[parent2_index]

    # Cruza
    hijo1, hijo2 = cruza(parent1, parent2)

    # Mutación
    hijo1 = mutacion(hijo1, tasa_mutacion)
    hijo2 = mutacion(hijo2, tasa_mutacion)

    # Reemplazar los padres con los hijos
    arreglo[parent1_index] = hijo1
    arreglo[parent2_index] = hijo2

    # Calcular y mostrar aptitudes
    """Se calcula la aptitud de todos los individuos y se elige el mejor"""
    for i, individuo in enumerate(arreglo, start=1):
        aptitud_individual = calcular_aptitud(individuo)
        print(f"La aptitud del individuo {i} es: {aptitud_individual}")

    individuo, aptitud = most_apt(arreglo)
    print("Individuo con mejor aptitud: ", individuo)
    print("Con una aptitud de: ", aptitud)

    print("Padre 1: ", parent1)
    print("Padre 2: ", parent2)
    print("Hijo 1: ", hijo1)
    print("Hijo 2: ", hijo2)

    # Representar la nueva población en binario
    el_binario = [[format(num, "04b") for num in individuo] for individuo in arreglo]
    print("Arreglo después de la cruza: ", el_binario)
    print("\n")
