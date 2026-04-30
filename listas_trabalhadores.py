salarios = []

for i in range(10):
    salario = float(input(f"Digite o salário do trabalhador {i+1}: R$ "))
    salarios.append(salario)

soma = 0
for s in salarios:
    soma += s

media = soma / 10

maior = salarios[0]
for s in salarios:
    if s > maior:
        maior = s

menor_850 = 0
for s in salarios:
    if s < 850:
        menor_850 += 1

print("\n RESULTADOS")
print("Salários:", salarios)
print("Média dos salários: R$ {:.2f}".format(media))
print("Maior salário: R$ {:.2f}".format(maior))
print("Quantidade de salários menores que R$ 850,00:", menor_850)