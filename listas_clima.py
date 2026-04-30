dias = []

chuvas = []



for i in range(10):

    print("\nDia", i + 1)

    dia = input("Digite o dia da semana: ").lower()

    volume = float(input("Digite o volume de chuva: "))

    

    dias.append(dia)

    chuvas.append(volume)



soma_total = 0

soma_quarta = 0

cont_quarta = 0



for i in range(10):

    soma_total += chuvas[i]

    

    if dias[i] == "quarta-feira" or dias[i] == "quarta":

        soma_quarta += chuvas[i]

        cont_quarta += 1



if cont_quarta > 0:

    media_quarta = soma_quarta / cont_quarta

else:

    media_quarta = 0



print("\n RESULTADOS ")

print("Soma total do volume de chuva:", soma_total)



if cont_quarta > 0:

    print("Média de chuva nas quartas-feiras:", media_quarta)

else:

    print("Não houve dados para quarta-feira.")