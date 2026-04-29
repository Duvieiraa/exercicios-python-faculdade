n = int(input("Digite um número inteiro positivo: "))

soma = 0

for i in range(1, n + 1):
    soma += 1 / i

print("O valor de S é:", soma)