def mostrar_menu():
    print("\n1- Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")

def somar(num1, num2):

    return num1 +num2

def subtrair(num1, num2):
    
    return num1 - num2

def multi(num1, num2):

    return num1 * num2

def divisao(num1, num2):
    
    return num1 / num2

mostrar_menu()
opcao = int(input("Bem-Vindo a sua calculadora! Escolha a opção que deseja: "))

while opcao != 0:

    if opcao == 1:

        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        resultado = somar(num1, num2) # aqui eu nao posso inserir os valores, porque desconsidera o que a pessoa escreveu
        print(resultado)

    elif opcao == 2:

        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        resultado = subtrair(num1, num2) # aqui eu nao posso inserir os valores, porque desconsidera o que a pessoa escreveu
        print(resultado)

    elif opcao == 3:

        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        resultado = multi(num1, num2)
        print(resultado)

    elif opcao == 4:

        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        resultado = divisao(num1, num2)
        print(resultado)

    else:

        print("opção inválida")

    opcao = int(input("Bem-Vindo a sua calculadora! Escolha a opção que deseja: "))

print("Programa encerrado")