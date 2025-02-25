"""
Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
"""
# Solicita um número inteiro ao usuário
num = int(input("Digite um número inteiro: "))

# Lista para armazenar os números primos encontrados
primos = []

# Percorre todos os números de 2 até o número informado
for n in range(2, num + 1):
    # Assume que o número é primo
    primo = True

    # Verifica se há divisores além de 1 e ele mesmo
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            primo = False
            break  # Se encontrou um divisor, pode parar

    # Se for primo, adiciona à lista
    if primo:
        primos.append(n)

# Exibe a lista de números primos
print(f"Números primos entre 1 e {num}: {primos}")
