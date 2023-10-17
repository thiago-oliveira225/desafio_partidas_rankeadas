while True:

    numVitoria = int(input("Digite o numero de vitoria = "))
    numDerrota = int(input("Digite o numero de derrota = "))

    def soma(num1, num2):#dentro do parenteses é a variavel
        resultado = num1 - num2
        if (resultado <= 10):
            print (f"O Herói tem de saldo de {resultado} vitórias está no nível de Ferro")
        elif (resultado >= 11 and resultado <= 20):
            print (f"O Herói tem de saldo de {resultado} vitórias está no nível de Bronze")
        elif (resultado >= 21 and resultado <= 50):
            print (f"O Herói tem de saldo de {resultado} vitórias está no nível de Prata")
        elif (resultado >= 51 and resultado <= 80):
            print (f"O Herói tem de saldo de {resultado} vitórias está no nível de Ouro")   
        elif (resultado >= 81 and resultado <= 90):
            print (f"O Herói tem de saldo de {resultado} vitórias está no nível de Diamante")
        elif (resultado >= 91 and resultado <= 100):
            print (f"O Herói de nome {resultado} vitórias está no nível de Lendário")
        elif (resultado > 100):
            print (f"O Herói de nome {resultado} vitórias está no nível de Imortal")

    soma(numVitoria,numDerrota) 