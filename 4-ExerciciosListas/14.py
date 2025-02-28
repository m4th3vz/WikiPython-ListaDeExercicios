"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    a."Telefonou para a vítima?"
    b."Esteve no local do crime?"
    c."Mora perto da vítima?"
    d."Devia para a vítima?"
    e."Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
def classificar_participacao(respostas):
    pontuacao = respostas.count("s")
    
    if pontuacao == 5:
        return "Assassino"
    elif 3 <= pontuacao <= 4:
        return "Cúmplice"
    elif pontuacao == 2:
        return "Suspeita"
    else:
        return "Inocente"

def main():
    perguntas = [
        "Telefonou para a vítima?",
        "Esteve no local do crime?",
        "Mora perto da vítima?",
        "Devia para a vítima?",
        "Já trabalhou com a vítima?"
    ]
    
    respostas = []
    for pergunta in perguntas:
        while True:
            resposta = input(f"{pergunta} (s/n): ").strip().lower()
            if resposta in ("s", "n"):
                respostas.append(resposta)
                break
            print("Por favor, responda apenas com 's' para sim ou 'n' para não.")
    
    classificacao = classificar_participacao(respostas)
    print(f"Classificação: {classificacao}")

if __name__ == "__main__":
    main()
