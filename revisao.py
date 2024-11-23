num = int(input("Digite um número:"))
numeros = []

for i in range(num):
    num -= 1
    numeros.append(num)

soma = sum(numeros) + num

print("soma",soma)