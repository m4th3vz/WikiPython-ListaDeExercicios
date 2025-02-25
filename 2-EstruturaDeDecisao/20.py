"""
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
    a.A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    b.A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    c.A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""
# Solicita as três notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

# Estrutura de decisão para verificar a situação do aluno
if media == 10:
    print(f"Aprovado com Distinção! Média: {media:.2f}")
elif media >= 7:
    print(f"Aprovado! Média: {media:.2f}")
else:
    print(f"Reprovado! Média: {media:.2f}")
