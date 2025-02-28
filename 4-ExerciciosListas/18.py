"""
Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
O total de votos computados;
Os númeos e respectivos votos de todos os jogadores que receberam votos;
O percentual de votos de cada um destes jogadores;
O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
"""
def calcular_percentual(votos, total_votos):
    return (votos / total_votos) * 100

def main():
    # Inicializa o array de votos
    votos = [0] * 23  # Lista de 23 posições para os jogadores 1 a 23

    while True:
        try:
            # Solicita o número do jogador
            jogador = int(input("Número do jogador (0=fim): "))
            
            # Se o número for 0, encerra a votação
            if jogador == 0:
                break
            
            # Verifica se o número é válido
            if 1 <= jogador <= 23:
                votos[jogador - 1] += 1  # Incrementa o voto do jogador
            else:
                print("Informe um valor entre 1 e 23 ou 0 para sair!")
        
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")

    # Total de votos computados
    total_votos = sum(votos)
    
    # Exibe o resultado
    print("\nResultado da votação:")
    print(f"\nForam computados {total_votos} votos.\n")
    
    # Lista para armazenar os jogadores com votos
    jogadores_com_votos = []
    
    for i in range(23):
        if votos[i] > 0:
            jogador_num = i + 1
            percentual = calcular_percentual(votos[i], total_votos)
            jogadores_com_votos.append((jogador_num, votos[i], percentual))
    
    # Ordena os jogadores pelo número
    jogadores_com_votos.sort(key=lambda x: x[0])

    # Exibe os votos e percentuais
    for jogador in jogadores_com_votos:
        print(f"{jogador[0]:<15}{jogador[1]:<10}{jogador[2]:.1f}%")
    
    # Encontra o melhor jogador
    melhor_jogador = max(jogadores_com_votos, key=lambda x: x[1])
    print(f"\nO melhor jogador foi o número {melhor_jogador[0]}, com {melhor_jogador[1]} votos, correspondendo a {melhor_jogador[2]:.1f}% do total de votos.")
    
    # Grava o resultado em um arquivo
    with open("resultado_votacao.txt", "w") as f:
        f.write(f"Resultado da votação:\n\n")
        f.write(f"Foram computados {total_votos} votos.\n\n")
        for jogador in jogadores_com_votos:
            f.write(f"Jogador {jogador[0]}: {jogador[1]} votos - {jogador[2]:.1f}%\n")
        f.write(f"\nO melhor jogador foi o número {melhor_jogador[0]}, com {melhor_jogador[1]} votos, correspondendo a {melhor_jogador[2]:.1f}% do total de votos.\n")
    
    print("\nResultado gravado no arquivo 'resultado_votacao.txt'.")

# Chama a função principal
if __name__ == "__main__":
    main()
