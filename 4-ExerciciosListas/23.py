"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.
"""
def bytes_para_mb(bytes):
    """Converte bytes para megabytes (MB)."""
    return bytes / (1024 * 1024)

def calcular_percentual(uso, total):
    """Calcula o percentual de uso baseado no uso individual e total."""
    return (uso / total) * 100

def gerar_relatorio(usuarios, total_uso):
    """Gera o relatório formatado e salva no arquivo 'relatório.txt'."""
    with open('relatório.txt', 'w') as f:
        f.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")
        f.write("------------------------------------------------------------------------\n")
        f.write("Nr.  Usuário        Espaço utilizado     % do uso\n")
        
        for i, (usuario, uso) in enumerate(usuarios.items(), start=1):
            mb = bytes_para_mb(uso)
            percentual = calcular_percentual(uso, total_uso)
            f.write(f"{i:<4} {usuario:<15} {mb:>10.2f} MB            {percentual:>6.2f}%\n")

        f.write("\n")
        f.write(f"Espaço total ocupado: {bytes_para_mb(total_uso):.2f} MB\n")
        f.write(f"Espaço médio ocupado: {bytes_para_mb(total_uso) / len(usuarios):.2f} MB\n")

def main():
    usuarios = {}
    total_uso = 0
    
    # Lê o arquivo 'usuarios.txt'
    with open('usuarios.txt', 'r') as f:
        for linha in f:
            # Lê nome e uso de cada usuário
            nome, uso = linha[:15].strip(), int(linha[15:].strip())
            usuarios[nome] = uso
            total_uso += uso
    
    # Gera o relatório
    gerar_relatorio(usuarios, total_uso)

# Chama a função principal
if __name__ == "__main__":
    main()
