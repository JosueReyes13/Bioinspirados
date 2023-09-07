import random

individuos = 30
los_bits = 1
el_rango = range(0, 15)

def caulcular_aptitud(individuo):
    aptitud = sum([x**2 + 2 for x in individuo])
    return aptitud
def most_apt(arreglo):
    apts = [caulcular_aptitud(individuo) for individuo in arreglo]
    better_index = apts.index(max(apts))
    return arreglo[better_index], apts[better_index]
def cruza(padre1, padre2):
    cross_point = random.randint(1, len(padre1))
    hijo1 = padre1[:cross_point] + padre2[cross_point:]
    hijo2 = padre2[:cross_point] + padre1[cross_point:]
    return hijo1, hijo2


arreglo = [[random.choice(el_rango) for i in range(los_bits)] for i in range(individuos)]
el_binario = [[format(num, "04b") for num in individuo] for individuo in arreglo]
# 0 indica los 0 a la izq que debe tener 
# 4 indica el resultado final, una longitud de 4 caracteres
# b indica como debe formatearse, en este caso, binario 



print(el_binario)
print("\n")

parent1_index = 0
parent2_index = 1

parent1 = arreglo[parent1_index]
parent2 = arreglo[parent2_index]

hijo1, hijo2 =cruza(parent1, parent2)

arreglo[parent1_index] = hijo1
arreglo[parent2_index] = hijo2


for i, individuo in enumerate(arreglo, start=1):
    aptitud_indivudual = caulcular_aptitud (individuo)
    print(f"La aptitud es {i}: {aptitud_indivudual}")

individuo, aptitud = most_apt(arreglo)
print("Aptitud del individuo con mejor apt: ", individuo)
print("Con una aptitud de: ", aptitud)

print("Padre 1: ", parent1)
print("Padre 2: ", parent2)
print("Hijo 1: ", hijo1)
print("Hijo 2", hijo2)
el_binario = [[format(num, "04b") for num in individuo] for individuo in arreglo]
print("Arreglo despues de la cruza: ", el_binario)

    