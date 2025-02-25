"""
Faça um programa que leia e valide as seguintes informações:
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';
"""
# Valida Nome (maior que 3 caracteres)
while True:
    nome = input("Nome (mais de 3 caracteres): ")
    if len(nome) > 3:
        break
    print("Nome inválido. Digite novamente.")

# Valida Idade (entre 0 e 150)
while True:
    idade = input("Idade (entre 0 e 150): ")
    if idade.isdigit() and 0 <= int(idade) <= 150:
        idade = int(idade)
        break
    print("Idade inválida. Digite novamente.")

# Valida Salário (maior que zero)
while True:
    salario = input("Salário (maior que zero): ")
    try:
        salario = float(salario)
        if salario > 0:
            break
    except ValueError:
        pass  # Se der erro ao converter, continua pedindo
    print("Salário inválido. Digite novamente.")

# Valida Sexo ('f' ou 'm')
while True:
    sexo = input("Sexo (f ou m): ").lower()
    if sexo in ("f", "m"):
        break
    print("Sexo inválido. Digite novamente.")

# Valida Estado Civil ('s', 'c', 'v', 'd')
while True:
    estado_civil = input("Estado Civil (s, c, v, d): ").lower()
    if estado_civil in ("s", "c", "v", "d"):
        break
    print("Estado Civil inválido. Digite novamente.")

# Exibe os dados validados
print("\nDados Validados:")
print("Nome:", nome)
print("Idade:", idade)
print("Salário:", salario)
print("Sexo:", sexo)
print("Estado Civil:", estado_civil)
