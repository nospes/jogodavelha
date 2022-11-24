import random
i = 0
def pedra_papel_tesouraPC():
    a = 0
    pontosjogador = 0
    pontoscomputador = 0
    jogos = int(input("Quantos Rounds? 1/3/5 "))

    if(jogos>5):
        jogos = 5

    while a < jogos:
        escolhajogador = input("pedra papel ou tesoura? ")
        if(escolhajogador=="Pedra" or escolhajogador=="pedra"):
            escolhajogador = 1
        elif(escolhajogador=="Tesoura" or escolhajogador=="tesoura"):
            escolhajogador = 2
        elif(escolhajogador=="Papel" or escolhajogador=="papel"):
            escolhajogador = 3
        escolhamaquina = random.randint(1,3)

        if(escolhajogador==escolhamaquina):
            print("Empate!")

            #Jogador Escolheu Pedra
        if(escolhajogador==1 and escolhamaquina==2):
            print("Ponto para jogador!")
            a+=1
            pontosjogador += 1
        if(escolhajogador==1 and escolhamaquina==3):
            print("Ponto para Máquina!")
            a+=1
            pontoscomputador += 1

            #Jogador Escolheu Tesoura
        if(escolhajogador==2 and escolhamaquina==1):
            print("Ponto para Máquina!")
            a+=1
            pontoscomputador += 1
        if(escolhajogador==2 and escolhamaquina==3):
            print("Ponto para Jogador!")
            a+=1
            pontosjogador += 1

            #Jogador Escolheu Papel
        if(escolhajogador==3 and escolhamaquina==1):
            print("Ponto para jogador!")
            a+=1
            pontosjogador += 1
        if(escolhajogador==3 and escolhamaquina==2):
            print("Ponto para Máquina!")
            a+=1
            pontoscomputador += 1

    if(pontoscomputador>pontosjogador):
        print("Vitoria do Computador!")
    elif(pontosjogador>pontoscomputador):      
        print("Vitoria do jogador!") 
    elif(pontoscomputador==pontosjogador):
        print("Empate Total")


def pedra_papel_tesouraPL():
    a = 0
    pontosjogador = 0
    pontosjogador2 = 0
    jogos = int(input("Quantos Rounds? 1/3/5 "))

    if(jogos>5):
        jogos = 5

    while a < jogos:
        escolhajogador = input("JOGADOR 1:pedra papel ou tesoura? ")
        if(escolhajogador=="Pedra" or escolhajogador=="pedra"):
            escolhajogador = 1
        elif(escolhajogador=="Tesoura" or escolhajogador=="tesoura"):
            escolhajogador = 2
        elif(escolhajogador=="Papel" or escolhajogador=="papel"):
            escolhajogador = 3
        
        escolhajogador2 = input("JOGADOR 2:pedra papel ou tesoura? ")
        if(escolhajogador2=="Pedra" or escolhajogador2=="pedra"):
            escolhajogador2 = 1
        elif(escolhajogador2=="Tesoura" or escolhajogador2=="tesoura"):
            escolhajogador2 = 2
        elif(escolhajogador2=="Papel" or escolhajogador2=="papel"):
            escolhajogador2 = 3

        if(escolhajogador==escolhajogador2):
            print("Empate!")

            #Jogador Escolheu Pedra
        if(escolhajogador==1 and escolhajogador2==2):
            print("Ponto para jogador 1!")
            a+=1
            pontosjogador += 1
        if(escolhajogador==1 and escolhajogador2==3):
            print("Ponto para jogador 2!")
            a+=1
            pontosjogador2 += 1

            #Jogador Escolheu Tesoura
        if(escolhajogador==2 and escolhajogador2==1):
            print("Ponto para jogador 2!")
            a+=1
            pontosjogador2 += 1
        if(escolhajogador==2 and escolhajogador2==3):
            print("Ponto para jogador 1!")
            a+=1
            pontosjogador += 1

            #Jogador Escolheu Papel
        if(escolhajogador==3 and escolhajogador2==1):
            print("Ponto para jogador 1!")
            a+=1
            pontosjogador += 1
        if(escolhajogador==3 and escolhajogador2==2):
            print("Ponto para jogador 2!")
            a+=1
            pontosjogador2 += 1

    if(pontosjogador2>pontosjogador):
        print("Vitoria do jogador 2!")
    elif(pontosjogador>pontosjogador2):      
        print("Vitoria do jogador 1!") 
    elif(pontosjogador2==pontosjogador):
        print("Empate Total")
    

while i < 1:
    decisao = input("Gostaria de jogar? y/n ")
    if(decisao=="y"):
        decisaojogo = input("Contra um 'Jogador' ou um 'PC' ")
        if(decisaojogo=="PC" or decisaojogo=="pc" or decisaojogo=="Pc"):
            pedra_papel_tesouraPC()
        else:
            pedra_papel_tesouraPL()
    else:
        i = 1
