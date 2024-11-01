def soma(a,b):
    return a+b

def mult(x,y):
    return x*y

def math():
    while True:
        print("BEM VINDO A CALCULADORA")
        print("Escolha uma das opções: 1.Soma   2.Multiplicar  3.Sair")
        option = input("Digite a opção: ") 
        if option == "1" or option == "2":
            n1 = float(input("Digite o primeiro numero: "))
            n2 = float(input("Digite o segundo numero: "))
            if option == "1":
                print("Soma",n1,"+",n2,"=",soma(n1,n2))
            elif option == "2":
                print("Multipicação",n1,"*",n2,"=",mult(n1,n2))
        elif option == "3":
            break 
        else:
            print("entrada invalida")

math()

    