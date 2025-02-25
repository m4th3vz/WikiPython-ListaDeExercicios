"""
Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
    o produto do dobro do primeiro com metade do segundo.
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo.
"""
# Função para validar entrada numérica genérica
def obter_numero(mensagem, tipo=float):
    while True:
        try:
            return tipo(input(mensagem))
        except ValueError:
            print(f"Entrada inválida! Digite um número {tipo.__name__} válido.")

# Solicita os números ao usuário
num1 = obter_numero("Digite um número inteiro: ", int)
num2 = obter_numero("Digite outro número inteiro: ", int)
num3 = obter_numero("Digite um número real: ", float)

# Cálculos
produto_dobro_metade = (num1 * 2) * (num2 / 2)
soma_triplo_terceiro = (num1 * 3) + num3
terceiro_ao_cubo = num3 ** 3

# Exibe os resultados formatados
print(
    f"O produto do dobro do primeiro com metade do segundo: {produto_dobro_metade:.2f}\n"
    f"A soma do triplo do primeiro com o terceiro: {soma_triplo_terceiro:.2f}\n"
    f"O terceiro elevado ao cubo: {terceiro_ao_cubo:.2f}"
)
