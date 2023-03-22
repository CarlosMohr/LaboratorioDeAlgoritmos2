numeros = []
for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

print("Os números digitados foram:")
for i, numero in enumerate(numeros):
    print(f"Posição {i+1}: {numero}")