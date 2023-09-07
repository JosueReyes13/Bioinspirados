import random

class Algoritmos_Bio:

    class AlgGen:
        individuos = 30
        los_bits_individuos = 4
        el_rango = range(0,15)

        arreglo = [[random.choice(el_rango) for _ in range(los_bits_individuos)] for _ in range(individuos)]
        print(arreglo)
