"""
Faça um Programa que peça um número e então mostre a mensagem
O número informado foi [número].
"""
while True:
    num = input("Digite um número: ")

    try:
        num = float(num)  # Converte para número (aceita inteiros e decimais)
        break  # Sai do loop se for um número válido
    except ValueError:
        print("Entrada inválida! Por favor, digite um número.")

print(f"O número informado foi {num}")
