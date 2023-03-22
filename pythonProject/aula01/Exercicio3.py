import random

tamanho_lista = int(input("Informe o tamanho da lista de números aleatórios: "))

lista_numeros = [random.randint(1, 1000) for i in range(tamanho_lista)]

print("Lista de números aleatórios: ", lista_numeros)