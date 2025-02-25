"""
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série.
"""
# Solicita ao usuário o número de termos da série
n = int(input("Digite a quantidade de termos da série: "))

# Inicializa a soma da série
soma = 0

# Inicializa a string para exibir a série formatada
serie = ""

# Calcula e exibe a série
for i in range(1, n + 1):
    numerador = i
    denominador = 2 * i - 1  # Fórmula do denominador: 1, 3, 5, 7, ...
    termo = numerador / denominador
    soma += termo  # Soma os termos

    # Formata a exibição da série
    serie += f"{numerador}/{denominador}"
    if i < n:
        serie += " + "

# Exibe os resultados
print(f"S = {serie}")
print(f"Soma da série = {soma:.4f}")  # Exibe a soma com 4 casas decimais
