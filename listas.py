valores = []
par = []
impar = []

while True:
    numero = int(input("Digite um número inteiro: "))
    valores.append(numero)
    
    continuar = input("Deseja continuar? (s/n): ").lower()
    if continuar != 's':
        break

for valor in valores:
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

print("\nLista de valores:", valores)
print("Lista de números pares:", par)
print("Lista de números ímpares:", impar)
