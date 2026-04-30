numeros = []

while True:
    num = float(input("Digite um número: "))
    numeros.append(num)
    
    continuar = input("Deseja continuar? (s/n): ").lower()
    if continuar != 's':
        break

soma = 0
for n in numeros:
    soma += n

if len(numeros) > 0:
    media = soma / len(numeros)
else:
    media = 0

acima_media = 0
for n in numeros:
    if n > media:
        acima_media += 1

print("\n RESULTADOS ")
print("Lista:", numeros)
print("Soma:", soma)
print("Média:", media)
print("Quantidade acima da média:", acima_media)