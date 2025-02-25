"""
Faça um Programa que peça dois números e imprima a soma.
"""
while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        break  # Sai do loop se os números forem válidos
    except ValueError:
        print("Entrada inválida! Por favor, digite apenas números.")

soma = num1 + num2
print(f"A soma entre {num1} e {num2} é {soma}")
