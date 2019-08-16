# -- coding: utf-8 --
import time
import os
import IP2Location
import re

clear = lambda: os.system("cls")
check = False
conteudo = ""
achou = int = 0
adiMais = "S"
proMais = "S"
database = IP2Location.IP2Location(os.path.join("data", "IP2LOCATION-LITE-DB11.BIN"))


print("Antes de comecar a procura, por favor cole o Header do E-mail no arquivo chamado Header.txt \n ")
while check == False:
    #Escolhas para o Usuario para a procura dos pontos principais do Header

    Escolha = float(input(
        "Selecione alguma das opções abaixo: \n 1- Verifição de endereço do Remetente \n 2- Verificar IP de origem \n 3- Verificar o Message-ID \n 4-Verificacao de quem foi enviado \n "))

    # Condicoes para a procura do algoritimo
    if Escolha == 1:
        clear()
        print("Abrindo sistema para PROCURAR o endereco do Remetente...")
        time.sleep(2)
        while proMais == "S":
            clear()
            #Palavra-Chave
            procurando = "Received: "
            #Lugar da procura
            with open("Header.txt", "r") as arq:
                for linha in arq:
                    if linha.find(procurando) > -1:
                        print(linha)
                        achou += 1
            print("Tarefa concluida.\n")
            if achou <= 0:
                print("Não foi possivel procurar um endereco de Remetente, por favor tente denovo.\n")
            elif achou == 1:
                print("Foi encontrado", achou, " Remetente.\n")
            else:
                print("Foram encontrados", achou, " Remententes.\n")
            achou = 0
            proMais = input("Você precisa procurar mais alguma informacao do Header? \n (S/N) \n").upper()


    elif Escolha == 2:
        clear()
        print("Abrindo sistema para PROCURAR o IP do Remetente...")
        time.sleep(2)
        while proMais == "S":
            clear()
            procurando = "IP"
            #print(procurando)
            with open("Header.txt", "r") as arq:
                for linha in arq:
                    if linha.find(procurando) > -1:
                        #print(linha)
                        ipResult = re.findall(r'[0-9]+(?:\.[0-9]+){3}', linha)
                        ipResult2 = (', '. join(ipResult))
            print("O seu endereço IP é: ", ipResult2)
            rec = database.get_all(ipResult2)
            print("Ele está localizado no seguinte país: ", rec.country_long)
            print("Na seguinte cidade: ", rec.city)
            #print("O seu IP resultante é: ", (', '.join(ipResult)) )
            achou += 1
            #rec = database.get_all(ipResult)
            print("Tarefa concluida.\n")
            if achou <= 0:
                print("Não foi possivel procurar um IP do Remetente, por favor tente denovo.\n")
            elif achou == 1:
                print("Foi encontrado", achou, " o IP.\n")
            else:
                print("Foram encontrados", achou, " IP's.\n")
            achou = 0
            proMais = input("Você precisa procurar mais alguma informacao do Header? \n (S/N) \n").upper()


    elif Escolha == 3:

        clear()

        print("Abrindo sistema para PROCURAR o ID da Mensagem...")

        time.sleep(2)

        while proMais == "S":

            clear()

            procurando = "Message-ID"

            # print(procurando)

            with open("Header.txt", "r") as arq:

                for linha in arq:

                    if linha.find(procurando) > -1:
                        print(linha)

            achou += 1

            # rec = database.get_all(ipResult)

            print("Tarefa concluida.\n")

            if achou <= 0:

                print("Não foi possivel procurar o Message- ID do Remetente, por favor tente denovo.\n")

            elif achou == 1:

                print("Foi encontrado", achou, " Message-ID.\n")

            else:

                print("Foram encontrados", achou, " Messages-ID.\n")

            achou = 0

            proMais = input("Você precisa procurar mais alguma informacao do Header? \n (S/N) \n").upper()

    elif Escolha == 4:

        clear()

        print("Abrindo sistema para PROCURAR o ID da Mensagem...")

        time.sleep(2)

        while proMais == "S":

            clear()

            procurando = "From"

            # print(procurando)

            with open("Header.txt", "r") as arq:

                for linha in arq:

                    if linha.find(procurando) > -1:
                        print(linha)

            achou += 1

            # rec = database.get_all(ipResult)

            print("Tarefa concluida.\n")

            if achou <= 0:

                print("Não foi possivel procurar o Message- ID do Remetente, por favor tente denovo.\n")

            elif achou == 1:

                print("Foi encontrado", achou, " Message-ID.\n")

            else:

                print("Foram encontrados", achou, " Messages-ID.\n")

            achou = 0

            proMais = input("Você precisa procurar mais alguma informacao do Header? \n (S/N) \n").upper()

    else:
        clear()
        Escolha = int(input(
            "Opção Inválida, Escolha corretamente:\n 1- Verifição de endereço do Remetente \n 2- Verificar IP de origem \n 3- Verificar o Message-ID \n 4-Verificacao de quem foi enviado \n "))
    algo = input("Precisa fazer mais alguma coisa? \n (S/N) \n").upper()

    if algo =="S":
        check = False
        clear()
    else:
        clear()
        check = True
        print("Obrigado, ate a próxima!")

