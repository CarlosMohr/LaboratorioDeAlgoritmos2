numeros = []
for i in range(4):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)
numeros.sort()
print(f'\n> Ordem menor para maior: {numeros}')
