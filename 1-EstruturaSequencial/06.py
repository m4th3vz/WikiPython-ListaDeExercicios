"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
import math

while True:
    try:
        raio = float(input("Digite o raio do círculo: "))
        if raio > 0:
            break  # Sai do loop se o valor for válido
        else:
            print("O raio deve ser um número positivo.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número válido.")

area = math.pi * (raio ** 2)
print(f"A área de um círculo de raio {raio} é {area:.2f}m².")
