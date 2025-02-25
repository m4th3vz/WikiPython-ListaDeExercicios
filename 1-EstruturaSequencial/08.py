"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""
while True:
    try:
        salario_hora = float(input("Digite quanto você ganha por hora: "))
        if salario_hora > 0:
            break
        else:
            print("O valor por hora deve ser positivo.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número válido.")

while True:
    try:
        horas_trabalhadas_mes = float(input("Digite quantas horas você trabalhou esse mês: "))
        if horas_trabalhadas_mes > 0:
            break
        else:
            print("O número de horas trabalhadas deve ser positivo.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número válido.")

salario_total = salario_hora * horas_trabalhadas_mes
print(
    f"Ganhando R${salario_hora:.2f} a hora, tendo trabalhado "
    f"{horas_trabalhadas_mes} horas no mês, seu salário este mês "
    f"é de R${salario_total:.2f}."
)
