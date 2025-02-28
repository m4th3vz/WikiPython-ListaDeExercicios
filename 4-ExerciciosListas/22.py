"""
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
"""
def main():
    # Dicionário para armazenar os tipos de defeito e suas contagens
    defeitos = {
        "necessita da esfera": 0,
        "necessita de limpeza": 0,
        "necessita troca do cabo ou conector": 0,
        "quebrado ou inutilizado": 0
    }
    
    total_mouses = 0  # Contador para o total de mouses

    # Entrada de dados
    while True:
        # Lê o número de identificação do mouse
        id_mouse = int(input("Digite o número de identificação do mouse (0 para encerrar): "))
        
        # Verifica se a identificação é 0, o que encerra o programa
        if id_mouse == 0:
            break
        
        # Lê o tipo de defeito
        print("Tipos de defeitos:")
        print("1 - necessita da esfera")
        print("2 - necessita de limpeza")
        print("3 - necessita troca do cabo ou conector")
        print("4 - quebrado ou inutilizado")
        
        defeito = int(input("Digite o número correspondente ao defeito: "))
        
        # Atualiza a contagem do defeito
        if defeito == 1:
            defeitos["necessita da esfera"] += 1
        elif defeito == 2:
            defeitos["necessita de limpeza"] += 1
        elif defeito == 3:
            defeitos["necessita troca do cabo ou conector"] += 1
        elif defeito == 4:
            defeitos["quebrado ou inutilizado"] += 1
        else:
            print("Defeito inválido! Tente novamente.")
            continue
        
        # Atualiza o total de mouses
        total_mouses += 1

    # Exibe o relatório
    print("\nRelatório:")
    print(f"Quantidade de mouses: {total_mouses}\n")
    print(f"{'Situação':<40} {'Quantidade':<15} {'Percentual'}")
    for situacao, quantidade in defeitos.items():
        percentual = (quantidade / total_mouses) * 100 if total_mouses > 0 else 0
        print(f"{situacao:<40} {quantidade:<15} {percentual:.2f}%")

# Chama a função principal
if __name__ == "__main__":
    main()
