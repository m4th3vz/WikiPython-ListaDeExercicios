"""
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.
"""
a, b = 0, 1  

while a <= 500:  # Continua enquanto a ainda não ultrapassou 500
    print(a, end=" ")
    a, b = b, a + b  

print(a)  # Exibe o primeiro número maior que 500 (610)
