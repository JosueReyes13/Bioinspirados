import random

class SistemaInmunologico:
    def __init__(self):
        self.leucocitos = 1000  # Cantidad inicial de leucocitos
        self.temperatura = 37.0  # Temperatura corporal inicial

    def atacar_patogeno(self):
        # Simulación de respuesta inmunológica
        if self.leucocitos > 0:
            # El patógeno genera un ataque aleatorio
            ataque_patogeno = random.randint(10, 50)
            self.leucocitos -= ataque_patogeno
            print(f"El patógeno ataca y disminuye los leucocitos en {ataque_patogeno}.")
        else:
            print("El sistema inmunológico está debilitado. Necesitas descansar y recuperarte.")

    def regular_temperatura(self):
        # Simulación de regulación de temperatura
        if self.leucocitos < 500:
            # Si los leucocitos son bajos, la temperatura aumenta más rápido
            self.temperatura += random.uniform(0.2, 0.5)
        else:
            self.temperatura += random.uniform(0.1, 0.2)
        
        # Asegurarse de que la temperatura no exceda los límites
        self.temperatura = min(42.0, max(36.0, self.temperatura))

    def estado_actual(self):
        print(f"Leucocitos: {self.leucocitos}, Temperatura: {self.temperatura}")

# Simulación principal
sistema = SistemaInmunologico()

for _ in range(10):
    sistema.atacar_patogeno()
    sistema.regular_temperatura()
    sistema.estado_actual()
