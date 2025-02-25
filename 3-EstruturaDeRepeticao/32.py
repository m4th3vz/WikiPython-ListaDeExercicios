"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
    Fatorial de: 5
    5! =  5 . 4 . 3 . 2 . 1 = 120
"""
# Solicita um número inteiro ao usuário
num = int(input("Fatorial de: "))

# Inicializa o fatorial como 1
fatorial = 1

# Cria a representação da multiplicação
sequencia = ""

# Calcula o fatorial usando um loop
for i in range(num, 0, -1):
    fatorial *= i
    sequencia += str(i) + (" . " if i > 1 else "")

# Exibe o resultado no formato correto
print(f"{num}! = {sequencia} = {fatorial}")
