def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Erro: Divisão por zero!"

def calculadora():
    while True:
        print("Operações disponíveis:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        opcao = input("Digite o número para a operação correspondente: ")

        if opcao == '0':
            print("Encerrando a calculadora.")
            break
        elif opcao not in {'1', '2', '3', '4'}:
            print("Essa opção não existe.")
            continue

        num1 = float(input("Digite o primeiro valor: "))
        num2 = float(input("Digite o segundo valor: "))

        if opcao == '1':
            resultado = soma(num1, num2)
            print("Resultado:", resultado)
        elif opcao == '2':
            resultado = subtracao(num1, num2)
            print("Resultado:", resultado)
        elif opcao == '3':
            resultado = multiplicacao(num1, num2)
            print("Resultado:", resultado)
        elif opcao == '4':
            resultado = divisao(num1, num2)
            print("Resultado:", resultado)

        print()  # Linha em branco para separar as operações

# Chamar a função para iniciar a calculadora
calculadora()