#Elabore um programa em Python que implemente uma calculadora com as funções de somar, subtrair, multiplicar e dividir. O programa deverá solicitar ao usuário os dois valores, e perguntar qual a operação pretendida (‘+’, ‘-‘ , ‘*’ ou ‘/’ ) e a seguir calcular e mostrar o resultado.
num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
operacao = input("Digite a operação (+, -, * ou /): ")

if operacao == "+":
    resultado = num1 + num2
    print("Resultado:", resultado)

elif operacao == "-":
    resultado = num1 - num2
    print("Resultado:", resultado)

elif operacao == "*":
    resultado = num1 * num2
    print("Resultado:", resultado)

elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado:", resultado)
    else:
        print("Erro: divisão por zero.")

else:
    print("Operação inválida.")