"""
Faça um Programa que peça a temperatura em graus Fahrenheit,
transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""
while True:
    try:
        graus_farenheit = float(input("Digite a temperatura em Fahrenheit: "))
        break  # Sai do loop se o valor for válido
    except ValueError:
        print("Entrada inválida! Por favor, digite um número válido.")

graus_celsius = 5 * (graus_farenheit - 32) / 9
print(
    f"{graus_farenheit:.2f} graus Fahrenheit correspondem a "
    f"{graus_celsius:.2f} graus Celsius"
)
