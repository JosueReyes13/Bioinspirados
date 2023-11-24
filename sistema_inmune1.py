"""El algoritmo de sistema inmune es un algoritmo de aprendizaje
automatico inspirado en el sistema inmune humano, esto lo 
hace reconociendo y eliminando las sustancias extrañas 
conocidas como antígenos"""
import random

"""1. Generación de población inicial
Aqui se genera una población inicial de 100 linfocitos B, cada
uno es una solución posible al problema, en este caso, cada 
linfocito B es una lista de 5 valores, uno por cada
caracteristica"""

# Definimos las características del problema
caracteristicas = [1, 2, 3, 4, 5]

# Definimos la función que genera la población inicial
def generar_poblacion():
    return [[random.randint(0, 1) for _ in range(len(caracteristicas))] for _ in range(100)]

"""2. Se evalua la afinidad
Aqui se evalua la afinidad de cada linfocito B con el 
antigeno, la afinidad s una medida de cuán bien una solución 
se adapta al problema, en este caso la afinidad se calcula 
como la suma de los productos de cada caracteristica por
su valor correspondiente"""

# Evaluamos la afinidad de cada linfocito B con el antígeno
def evaluar_afinidad(linfocito):
    afinidad = 0
    for caracteristica, valor in zip(caracteristicas, linfocito):
        afinidad += caracteristica * valor
    return afinidad

"""3. Se selecciona los linfocitos B con mayor afinidad
Se selecciona a los linfocitos los cuales se concideran 
los mejores candidatos para resover el problema"""

# Seleccionamos los linfocitos B con mayor afinidad
def seleccionar(poblacion):
    return sorted(poblacion, key=evaluar_afinidad, reverse=True)

"""4. Mutaciones en los linfocitos B
Aqui se realizan las mutaciones en los linfocitos B para
generar nuevas soluciones, las mutaciones sirven para 
cambios aleatorios en los valores de los linfocitos B"""

# Realizamos mutaciones en los linfocitos B para generar nuevas soluciones
def mutar(linfocito):
    for i in range(len(linfocito)):
        if random.random() < 0.1:
            linfocito[i] = 1 - linfocito[i]
    return linfocito

"""5. Repetimos los paso de 2 a 4 hasta encontrar la mejor 
solución:
Esta linea de codigo se encarga de repetir los paso de 2 a 4 hasta
que se encuentre una solución satisfactoria, en este caso, una 
solución satisfactoria que tenga una afinidad de 10"""

# Recorremos los pasos del algoritmo hasta encontrar una solución satisfactoria
def main():
    # Definimos la población inicial
    poblacion = generar_poblacion()
    while True:
        # Evaluamos la afinidad de cada linfocito B con el antígeno
        poblacion = seleccionar(poblacion)

        # Seleccionamos los linfocitos B con mayor afinidad
        linfocitos_b = poblacion[:5]

        # Realizamos mutaciones en los linfocitos B para generar nuevas soluciones
        poblacion = [mutar(linfocito) for linfocito in linfocitos_b]

        # Si encontramos una solución satisfactoria, salimos del bucle
        if evaluar_afinidad(poblacion[0]) == 10:
            break

    print(poblacion[0])

if __name__ == "__main__":
    main()

"""Ejemplo de uso:
El objetivo es encontrar una afinidad total de 10, donde la
afinidad se calcula como la suma de los productos de cada
caracteristica por su valor correspondiete en una lista de 
caracteristicas. [1, 1, 1, 1, 1] esto significa que el 
algoritmo encontro una solución donde todas las caracteristicas
se establecen en 1, y la suma de los productos de estas
caracteristicas por sus valores correspondintes es igual a
10, 1*1 + 2*1 + 3*1 + 4*1 + 5*1 = 1 + 2 + 3 + 4 + 5 = 15
Dado que el objetivo es una afinidad de 10, es posible que 
el algoritmo realice varias iteraciones antes de encontrar 
una solución satisfactoria. La salida variará según la
ejecución específica del programa y la aleatoriedad 
involucrada en las mutaciones."""