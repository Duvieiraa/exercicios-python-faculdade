def multiplicar(a, b):
    return a * b

def subtrair(a, b, c):
    resultado = a - b - c
    return resultado

v1 = int(input("Digite o valor de a:"))
v2 = int(input("Digite o valor de b:"))
v3 = int(input("Digite o valor de c:"))


resultado_mult = multiplicar(v1, v2)

resultado_sub  = subtrair(v1,v2,v3)

print("O resultado da multiplicação é : ", resultado_mult)
print("O resultado da subtração é : ", resultado_sub)
 
