"""
Tendo como dados de entrada a altura de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58
"""
while True:
    try:
        altura = float(input("Digite sua altura em metros: "))
        if altura > 0:
            break  # Sai do loop se a altura for válida
        print("A altura deve ser um número positivo. Tente novamente.")
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

peso_ideal = (72.7 * altura) - 58
print(f"O peso ideal para sua altura de {altura:.2f}m é: {peso_ideal:.2f}Kg")
