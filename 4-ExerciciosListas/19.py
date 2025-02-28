"""
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
"""
def calcular_percentual(votos, total_votos):
    return (votos / total_votos) * 100

def main():
    # Inicializa o vetor de votos para cada opção
    votos = [0] * 6  # Cada índice corresponde a uma opção: 1-6
    
    while True:
        try:
            # Solicita o voto (número do sistema operacional)
            voto = int(input("Digite o número do Sistema Operacional (0 para encerrar): "))
            
            # Se o número for 0, encerra a coleta de dados
            if voto == 0:
                break
            
            # Verifica se o voto está dentro das opções válidas (1 a 6)
            if 1 <= voto <= 6:
                votos[voto - 1] += 1  # Incrementa o voto na opção correspondente
            else:
                print("Valor inválido. Por favor, escolha uma opção entre 1 e 6 ou 0 para encerrar.")
        
        except ValueError:
            print("Valor inválido. Por favor, digite um número inteiro.")

    # Calcula o total de votos
    total_votos = sum(votos)
    
    # Nome dos sistemas operacionais
    sistemas = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
    
    # Exibe a tabela de resultados
    print("\nSistema Operacional     Votos   %")
    print("-------------------     -----   ---")
    
    for i in range(6):
        percentual = calcular_percentual(votos[i], total_votos)
        print(f"{sistemas[i]:<22}{votos[i]:<7}{percentual:>3.0f}%")
    
    print("-------------------     -----")
    print(f"Total                    {total_votos}")

    # Encontra o vencedor
    vencedor_index = votos.index(max(votos))
    vencedor = sistemas[vencedor_index]
    vencedor_votos = votos[vencedor_index]
    vencedor_percentual = calcular_percentual(vencedor_votos, total_votos)

    # Exibe o vencedor
    print(f"\nO Sistema Operacional mais votado foi o {vencedor}, com {vencedor_votos} votos, correspondendo a {vencedor_percentual:.0f}% dos votos.")

# Chama a função principal
if __name__ == "__main__":
    main()
