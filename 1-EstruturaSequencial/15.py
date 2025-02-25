"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês.

Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
while True:
    try:
        preco_hora = float(input("Digite quanto você ganha por hora: "))
        if preco_hora <= 0:
            print("O valor deve ser positivo. Tente novamente.")
            continue
        break
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

while True:
    try:
        horas_trabalhadas = float(input("Digite quantas horas você trabalhou esse mês: "))
        if horas_trabalhadas <= 0:
            print("O valor deve ser positivo. Tente novamente.")
            continue
        break
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

salario_bruto = preco_hora * horas_trabalhadas
IR = salario_bruto * 0.11
INSS = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (IR + INSS + sindicato)

print(
    f"+ Salário Bruto : R${salario_bruto:.2f}\n"
    f"- IR (11%) : R${IR:.2f}\n"
    f"- INSS (8%) : R${INSS:.2f}\n"
    f"- Sindicato (5%) : R${sindicato:.2f}\n"
    f"= Salário Líquido : R${salario_liquido:.2f}"
)
