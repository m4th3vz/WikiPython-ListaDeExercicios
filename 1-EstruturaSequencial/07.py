"""
Faça um Programa que calcule a área de um quadrado,
em seguida mostre o dobro desta área para o usuário.
"""
while True:
    try:
        lado = float(input("Digite o lado do quadrado: "))
        if lado > 0:
            break  # Sai do loop se o valor for válido
        else:
            print("O lado do quadrado deve ser um número positivo.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número válido.")

area = lado ** 2
dobro = area * 2
print(f"O dobro da área de um quadrado de lado {lado:.2f}m é {dobro:.2f}m²")
