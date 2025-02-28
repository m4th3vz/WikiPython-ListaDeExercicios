"""
Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
O modelo do carro mais econômico;
Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.
Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: Vectra
Km por litro: 9
Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
O menor consumo é do peugeout.
"""
def main():
    # Listas com os modelos e consumos dos carros
    carros = ['fusca', 'gol', 'uno', 'vectra', 'peugeot']
    consumos = [7, 10, 12.5, 9, 14.5]

    preco_gasolina = 2.25  # preço da gasolina por litro
    distancia = 1000  # distância fixa de 1000 km

    # Variáveis para armazenar o carro mais econômico
    carro_mais_economico = ""
    menor_consumo = float('inf')

    # Exibindo a tela inicial
    print("Comparativo de Consumo de Combustível\n")
    
    # Laço para calcular o consumo de combustível para 1000 km e custo
    for i in range(len(carros)):
        km_por_litro = consumos[i]
        litros_consumidos = distancia / km_por_litro
        custo = litros_consumidos * preco_gasolina
        
        # Exibindo informações do carro
        print(f"Veículo {i+1}")
        print(f"Nome: {carros[i]}")
        print(f"Km por litro: {km_por_litro}")
        print()

        # Determinando o carro mais econômico
        if km_por_litro < menor_consumo:
            menor_consumo = km_por_litro
            carro_mais_economico = carros[i]

        # Exibindo o relatório final
        print(f"Relatório Final")
        for j in range(len(carros)):
            km_por_litro = consumos[j]
            litros_consumidos = distancia / km_por_litro
            custo = litros_consumidos * preco_gasolina
            print(f"{j+1} - {carros[j]:<12} - {km_por_litro:<5} - {litros_consumidos:<10.1f} litros - R$ {custo:<7.2f}")
            print(f"O menor consumo é do {carro_mais_economico}.")
        
        

# Chama a função principal
if __name__ == "__main__":
    main()
