"""
Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
"""
# Solicita um número inteiro ao usuário
num = int(input("Digite um número inteiro: "))

# Números menores que 2 não são primos
if num < 2:
    print(f"{num} não é um número primo.")
else:
    # Assume que o número é primo
    primo = True

    # Verifica se há divisores além de 1 e ele mesmo
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break  # Se encontrou um divisor, pode parar

    # Exibe o resultado
    if primo:
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é um número primo.")
