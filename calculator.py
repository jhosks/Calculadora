# Funções de operação matemática
def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    else:
        return x / y

while True:
    # Exibe o Menu
    print("Selecione a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    # Solicita ao usuário que escolha uma operação
    operacao = input("Escolha a opção (1/2/3/4/5): ")

    # Verifica se a escolha é válida
    if operacao in ('1', '2', '3', '4', '5'):
        if operacao == '5':
            break
        else:
            # Solicita ao usuário que insira os números
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            
            # Realiza a operação com base na escolha do usuário
            if operacao == '1':
                print("Resultado: ", adicao(n1, n2))
            elif operacao == '2':
                print("Resultado: ", subtracao(n1, n2))
            elif operacao == '3':
                print("Resultado: ", multiplicacao(n1, n2))
            elif operacao == '4':
                print("Resultado: ", divisao(n1, n2))
            
            continuar = input("Deseja executar outra operação? (S / N): ")
            if continuar.upper() != 'S':
                break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida (1/2/3/4/5).")