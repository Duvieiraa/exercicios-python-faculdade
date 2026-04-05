produto = input("Digite o nome do produto: ")
valor_compra = float(input("Digite o valor de compra: "))

if valor_compra < 10:
    valor_venda = valor_compra * 1.70
elif valor_compra >= 10 and valor_compra < 30:
    valor_venda = valor_compra * 1.50
elif valor_compra >= 30 and valor_compra < 50:
    valor_venda = valor_compra * 1.40
else:
    valor_venda = valor_compra * 1.30

print("Produto:", produto)
print("Valor de venda: R$", valor_venda)