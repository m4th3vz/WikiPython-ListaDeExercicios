"""
Faça um Programa que converta metros para centímetros.
"""
while True:
    try:
        metros = float(input("Digite o valor em metros: "))
        if metros >= 0:
            break  # Sai do loop se o valor for válido
        else:
            print("Por favor, digite um valor positivo.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número válido.")

centimetros = metros * 100
print(f"{metros:.2f} metros equivalem a {centimetros:.2f} centímetros.")

