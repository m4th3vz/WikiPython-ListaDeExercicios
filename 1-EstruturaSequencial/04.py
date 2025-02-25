"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""
def obter_nota(unidade):
    while True:
        try:
            nota = float(input(f"Digite a nota da unidade {unidade}: "))
            if 0 <= nota <= 10:  # Garantir que a nota esteja no intervalo válido
                return nota
            else:
                print("Nota inválida! Digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido.")

nota1 = obter_nota(1)
nota2 = obter_nota(2)
nota3 = obter_nota(3)
nota4 = obter_nota(4)

media = (nota1 + nota2 + nota3 + nota4) / 4

print(
    f"A média das notas {nota1:.2f}, {nota2:.2f}, "
    f"{nota3:.2f} e {nota4:.2f} é {media:.2f}"
)
