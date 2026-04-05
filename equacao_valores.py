#Ler três valores inteiros (variáveis a, b e c) e efetuar o cálculo da equação de segundo grau, apresentando: as duas raízes, quando for possível efetuar o cálculo (delta positivo ou zero); a mensagem "Não há raízes reais", se não for possível fazer o cálculo (delta negativo); e a mensagem "Não é equação do segundo grau", se o valor de a for igual a zero.'  
import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a == 0:
    print("Não é equação do segundo grau.")
else:
    delta = (b ** 2) - (4 * a * c)
    
    print("Delta =", delta)
    
    if delta < 0:
        print("Não há raízes reais.")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        
        print("--- Resultado ---")
        print("Raiz 1:", x1)
        print("Raiz 2:", x2)