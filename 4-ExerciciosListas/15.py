"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
    a.Mostre a quantidade de valores que foram lidos;
    b.Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    c.Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    d.Calcule e mostre a soma dos valores;
    e.Calcule e mostre a média dos valores;
    f.Calcule e mostre a quantidade de valores acima da média calculada;
    g.Calcule e mostre a quantidade de valores abaixo de sete;
    h.Encerre o programa com uma mensagem;
"""
def main():
    notas = []
    
    while True:
        try:
            nota = float(input("Digite uma nota (-1 para encerrar): "))
            if nota == -1:
                break
            notas.append(nota)
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    
    if not notas:
        print("Nenhuma nota foi informada.")
        return
    
    quantidade = len(notas)
    soma = sum(notas)
    media = soma / quantidade
    acima_da_media = sum(1 for nota in notas if nota > media)
    abaixo_de_sete = sum(1 for nota in notas if nota < 7)
    
    print(f"Quantidade de valores lidos: {quantidade}")
    print("Valores informados:", " ".join(map(str, notas)))
    print("Valores na ordem inversa:")
    for nota in reversed(notas):
        print(nota)
    print(f"Soma dos valores: {soma:.2f}")
    print(f"Média dos valores: {media:.2f}")
    print(f"Quantidade de valores acima da média: {acima_da_media}")
    print(f"Quantidade de valores abaixo de sete: {abaixo_de_sete}")
    print("Programa encerrado. Obrigado por utilizar!")

if __name__ == "__main__":
    main()
