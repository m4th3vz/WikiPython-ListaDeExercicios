"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""
def main():
    while True:
        # Recebe o nome do atleta
        nome = input("Digite o nome do atleta (ou aperte enter para sair): ").strip()
        
        # Se o nome estiver vazio, encerra o programa
        if not nome:
            print("Programa encerrado.")
            break
        
        # Recebe as distâncias dos saltos
        saltos = []
        for i in range(1, 6):
            while True:
                try:
                    salto = float(input(f"Digite a distância do {i}º salto: ").replace(",", "."))
                    saltos.append(salto)
                    break
                except ValueError:
                    print("Valor inválido. Por favor, digite um número válido para a distância.")
        
        # Calcula a média dos saltos
        media = sum(saltos) / len(saltos)
        
        # Exibe o resultado
        print(f"\nResultado final:")
        print(f"Atleta: {nome}")
        print(f"Saltos: {' - '.join(map(str, saltos))}")
        print(f"Média dos saltos: {media:.1f} m\n")

# Chama a função principal
if __name__ == "__main__":
    main()
