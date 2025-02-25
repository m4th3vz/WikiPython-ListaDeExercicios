"""
Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
"""
while True:
    try:
        altura = float(input("Digite sua altura em metros: "))
        if altura > 0:
            break
        print("A altura deve ser um número positivo. Tente novamente.")
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

peso_ideal_homem = (72.7 * altura) - 58
peso_ideal_mulher = (62.1 * altura) - 44.7

print(
    f"O peso ideal para sua altura de {altura:.2f}m é:\n"
    f"- {peso_ideal_homem:.2f}Kg para homens\n"
    f"- {peso_ideal_mulher:.2f}Kg para mulheres"
)