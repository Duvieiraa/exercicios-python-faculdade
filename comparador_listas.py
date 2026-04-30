lista1 = []
lista2 = []

print("Digite 5 números inteiros para a primeira lista:")
for i in range(5):
    num = int(input(f"Valor {i+1}: "))
    lista1.append(num)

print("\nDigite 5 números inteiros para a segunda lista:")
for i in range(5):
    num = int(input(f"Valor {i+1}: "))
    lista2.append(num)

comuns = []

for elemento in lista2:
    if elemento in lista1:
        comuns.append(elemento)

print("\nPrimeira lista:", lista1)
print("Segunda lista:", lista2)

if len(comuns) == 0:
    print("Não há elemento em comum.")
else:
    print("Elementos em comum:", comuns)