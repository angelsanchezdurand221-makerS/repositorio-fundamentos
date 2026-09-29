import math

# 1. MODULARIDAD: Una función enfocada en una sola tarea
# 2. NOMBRES CLAROS: Nombres descriptivos de funciones y parámetros
def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_circulo(radio):
    # 3. ELIMINACIÓN DE REDUNDANCIAS:
    # Se usa la constante math.pi en lugar de escribir 3.14159 a mano
    # y se retorna el cálculo directamente sin guardar en variables intermedias
    return math.pi * (radio ** 2)

# Uso claro y legible
print(f"Área del rectángulo: {calcular_area_rectangulo(5, 10)}")
print(f"Área del triángulo: {calcular_area_triangulo(5, 10)}")
print(f"Área del círculo: {calcular_area_circulo(3):.2f}")