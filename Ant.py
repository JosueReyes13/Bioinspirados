"""Este algoritmo "Ant Colony" es un algoritmo
de optimiación el cual copia o simula el 
comportamiento de las hormigas en la vida
real, se basa en la idea de que las hormigas
pueden encontrar caminos cortos entre su nido 
y un alimento, esto con ayuda de feromonas que ellas
producen,"""

import random

"""1. Se crea una población de hormigas que se colocan
en un punto de partida, cada hormiga se asigna aleatorimente 
a una ciudad o una solución"""

ciudades = 5
hormigas = 10
iteraciones = 100
peso_feromona = 1.0 #Peso de la feromona
info_heuristica = 2.0 #Peso de la información heurística
evaporacion = 0.5 #Tasa de evaporación de feromonas
feromona_depositada = 1.0 #Cantidad de feromona depositada

distancias = [
    [0, 2, 9, 10, 7],
    [2, 0, 6, 4, 8],
    [9, 6, 0, 8, 10],
    [10, 4, 8, 0, 3],
    [7, 8, 10, 3, 0]
]

# Inicialización de feromonas en todas las aristas
feromonas = [[1.0 for _ in range(ciudades)] for _ in range(ciudades)]


"""2. Construcción de soluciones: Cada hormiga recorre
el espacio de soluciones, construyendo una posible solución
paso a paso.
- Explotación: Las hormigas tienden a seleccionar la mejor 
opción localmente.
- Exploración:Tienen en cuenta las feromonas depositadas en
las soluciones, lo que permite explorar nuevas posibilidades"""

# Función de probabilidad para elegir la siguiente ciudad
def calcular_probabilidad(hormiga, ciudad_actual, ciudades_no_visitadas):
    probabilidad = {}
    denominador = 0.0

    for ciudad in ciudades_no_visitadas:
        numerador = (feromonas[ciudad_actual][ciudad] * peso_feromona) * ((1.0 / distancias[ciudad_actual][ciudad]) * info_heuristica)
        probabilidad[ciudad] = numerador
        denominador += numerador

    for ciudad in ciudades_no_visitadas:
        probabilidad[ciudad] /= denominador

    return probabilidad

# Ciclo principal del ACO (Iteración)
for iteracion in range(iteraciones):
    rutas_hormigas = []  # Almacena las rutas de todas las hormigas en esta iteración

    # Construcción de soluciones para cada hormiga
    for _ in range(hormigas):
        ciudad_actual = random.randint(0, ciudades - 1)  # Inicialización

        ciudades_no_visitadas = set(range(ciudades))
        ciudades_no_visitadas.remove(ciudad_actual)
        ruta_hormiga = [ciudad_actual]

        while ciudades_no_visitadas:
            # Cálculo de probabilidad para la selección de la siguiente ciudad (Explotación y Exploración)
            probabilidades = calcular_probabilidad(_, ciudad_actual, ciudades_no_visitadas)
            ciudad_siguiente = random.choices(list(probabilidades.keys()), weights=list(probabilidades.values()))[0]

            ruta_hormiga.append(ciudad_siguiente)
            ciudades_no_visitadas.remove(ciudad_siguiente)
            ciudad_actual = ciudad_siguiente

        rutas_hormigas.append(ruta_hormiga)  # Almacena la ruta de la hormiga


"""3. Actualiación de las feromonas: Después de que las 
hormigas hayan construido sus soluciones, se actualizaran 
 las feromonas en función de la calidad de las soluciones
 encontradas, las feromonas evaporan con el tiempo para 
 evitar que el algoritmo se quede atrapado"""

for i in range(ciudades):
        for j in range(ciudades):
            if i != j:
                feromonas[i][j] *= (1 - evaporacion)  # Evaporación de feromonas

for ruta in rutas_hormigas:
    longitud_ruta = sum(distancias[ruta[i]][ruta[i + 1]] for i in range(ciudades - 1))
    longitud_ruta += distancias[ruta[-1]][ruta[0]]  # Para volver al punto de partida
    feromona_depositada = feromona_depositada / longitud_ruta

for i in range(ciudades):
    j = (i + 1) % ciudades
    feromonas[ruta[i]][ruta[j]] += feromona_depositada  # Depositar feromonas en la arista


"""4. Iteración: Los pasos 2 y 3 se repiten durante un numero
fijo de iteraciones o hasta que se alcance un criterio de 
parada"""

"""5. Mejor solución encontrada: A medida que avanza el 
algoritmo, se realiza un seguimiento de la mejor solución 
encontrda hasta el momento"""

# Encontrar la mejor solución (Mejor solución encontrada)
mejor_ruta = min(rutas_hormigas, key=lambda ruta: sum(distancias[ruta[i]][ruta[i + 1]] 
                                                      for i in range(ciudades - 1)) + distancias[ruta[-1]][ruta[0]])
print("La mejor ruta encontrada fue:", mejor_ruta)

"""6. Resultado final: Una vez que se completa el número
deseado de iteraciones, el algoritmo devuelve la mejor solución 
encontrada"""