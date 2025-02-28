"""
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
"""
import random

def lancar_dado():
    """Função para simular o lançamento de um dado (número aleatório de 1 a 6)."""
    return random.randint(1, 6)

def contar_lancamentos():
    """Função para realizar 100 lançamentos e contar as ocorrências de cada valor."""
    contadores = [0] * 6  # Lista com 6 elementos, cada um representando uma face do dado (1 a 6)
    
    # Realizar 100 lançamentos
    for _ in range(100):
        resultado = lancar_dado()
        contadores[resultado - 1] += 1  # Incrementa o contador para o número gerado
    
    # Exibir os resultados
    for i in range(6):
        print(f"O número {i+1} apareceu {contadores[i]} vezes.")

# Chama a função principal
contar_lancamentos()
