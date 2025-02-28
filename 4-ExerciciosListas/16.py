"""
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
    a.$200 - $299
    b.$300 - $399
    c.$400 - $499
    d.$500 - $599
    e.$600 - $699
    f.$700 - $799
    g.$800 - $899
    h.$900 - $999
    i.$1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
"""
def calcular_salario(vendas_brutas):
    return 200 + (0.09 * vendas_brutas)

def obter_posicao(salario):
    return min((int(salario) - 200) // 100, 8)

def main():
    contadores = [0] * 9  # Lista para contar vendedores em cada faixa salarial
    
    while True:
        try:
            vendas = input("Digite o valor das vendas brutas do vendedor (-1 para encerrar): ")
            if vendas == "-1":
                break
            
            vendas = float(vendas)
            salario = calcular_salario(vendas)
            posicao = obter_posicao(salario)
            contadores[posicao] += 1
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    
    faixas = [
        "$200 - $299", "$300 - $399", "$400 - $499", "$500 - $599",
        "$600 - $699", "$700 - $799", "$800 - $899", "$900 - $999",
        "$1000 em diante"
    ]
    
    print("\nDistribuição de salários:")
    for i, faixa in enumerate(faixas):
        print(f"{faixa}: {contadores[i]} vendedores")
    
    print("Programa encerrado. Obrigado por utilizar!")

if __name__ == "__main__":
    main()