positivos = 0
negativos = 0

valor = float(input("Digite um valor (0 para encerrar): "))

menor = valor

while valor != 0:
    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1

    if valor < menor:
        menor = valor

    valor = float(input("Digite um valor (0 para encerrar): "))

print("Quantidade de valores positivos:", positivos)
print("Quantidade de valores negativos:", negativos)

if positivos + negativos > 0:
    print("Menor valor digitado:", menor)
else:
    print("Nenhum valor válido foi digitado.")