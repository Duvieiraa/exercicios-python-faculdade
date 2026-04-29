soma_altura_homens = 0
soma_altura_mulheres = 0
qtd_homens = 0
qtd_mulheres = 0

sexo = int(input("Digite o sexo 1 para masculino e 2 para feminino ou '0' para encerrar: "))

while sexo != 0:
    altura = float(input("Digite a altura: "))

    if sexo == 1:
        soma_altura_homens += altura
        qtd_homens += 1
    elif sexo == 2:
        soma_altura_mulheres += altura
        qtd_mulheres += 1
    else:
        print("Sexo inválido!")

    sexo = int(input("Digite o sexo 1 para masculino e 2 para feminino ou '0' para encerrar: "))

if qtd_homens > 0:
    media_homens = soma_altura_homens / qtd_homens
    print("Altura média dos homens:", media_homens)
else:
    print("Nenhum homem foi informado.")

if qtd_mulheres > 0:
    media_mulheres = soma_altura_mulheres / qtd_mulheres
    print("Altura média das mulheres:", media_mulheres)
else:
    print("Nenhuma mulher foi informada.")