placas = []
multas = []

for i in range(15):
    print(f"\nCarro {i+1}")
    placa = input("Digite a placa: ")
    valor = float(input("Digite o valor da multa: R$ "))
    
    placas.append(placa)
    multas.append(valor)

soma = 0
maior_300 = 0

for valor in multas:
    soma += valor
    if valor >= 300:
        maior_300 += 1

media = soma / 15

print("\n RESULTADOS ")
print("Valor médio das multas: R$ {:.2f}".format(media))
print("Quantidade de multas >= R$ 300,00:", maior_300)