# JOGO DA VELHA
# FEITO EM UM TRABALHO DE P.O.O, DO CURSO DE TÉCNICO EM INFORMÁTICA PARA INTERNET
# PROF. ANDERSON
# INSTITUTO FEDERAL DE RONDÔNIA - ZONA NORTE - PORTO VELHO


# SÓ ACEITA ENTRADAS DE 1 A 9
# BLOQUEADA ENTRADA DUPLA
# RECONSTROI A TELA A CADA NOVA JOGADA, DANDO IMPRESSÃO DE CONTINUIDADE DO JOGO
# PODE SER JOGADA VÁRIAS PARTIDAS.

#####FALTA FAZER FUNÇÃO MULTIPLAYER

import os;
import get;


clear = lambda: os.system('cls')   #Cria uma funcão anônima

def verificaPosicao(pos):  #A CADA JOGADA VERIFICA SE A POSIÇÃO JÁ FOI UTILIZADA
    if velha1[pos] == " ":
        return 1 #verdadeiro
    else:
        return 2 #Falso

def converte(x): #Aqui recebe valor do teclado numérico e converte a posição

    if x == 1:
        posicao = 6
    elif x== 2:
        posicao = 7
    elif x== 3:
        posicao = 8
    elif x== 4:
        posicao = 3
    elif x== 5:
        posicao = 4
    elif x== 6:
        posicao = 5
    elif x== 7:
        posicao = 0
    elif x== 8:
        posicao = 1
    elif x== 9:
        posicao = 2

    return posicao

def mostraVelha():  # Mostra o desenho da Velha e instruções

    clear()  #função anonima sendo chamada para limpar a tela

    print('\n')
    linhaV1 = str(velha[0]) + ' | ' + str(velha[1]) + ' | ' + str(velha[2])
    linhaV2 = str(velha[3]) + ' | ' + str(velha[4]) + ' | ' + str(velha[5])
    linhaV3 = str(velha[6]) + ' | ' + str(velha[7]) + ' | ' + str(velha[8])

    linha1 = str(velha1[0]) + ' | ' + str(velha1[1]) + ' | ' + str(velha1[2]) + '                           ' + linhaV1
    linha2 = str(velha1[3]) + ' | ' + str(velha1[4]) + ' | ' + str(velha1[5]) + '                           ' + linhaV2
    linha3 = str(velha1[6]) + ' | ' + str(velha1[7]) + ' | ' + str(velha1[8]) + '                           ' + linhaV3

    print('                      TECLADO NUMÉRICO PARA ESCOLHA DA POSIÇÃO:\n')
    print(linha1)
    print('----------')
    print(linha2)
    print('----------')
    print(linha3)
    print('\n')


def verificaGanhador(jogador):  #verifica se o Jogador ganhou a cada jogada
    if   velha1[0] == jogador and velha1[1] == jogador and velha1[2] == jogador :
        return 1
    elif velha1[3] == jogador and velha1[4] == jogador and velha1[5] == jogador :
        return 1
    elif velha1[6] == jogador and velha1[7] == jogador and velha1[8] == jogador :
        return 1
    elif velha1[0] == jogador and velha1[3] == jogador and velha1[6] == jogador :
        return 1
    elif velha1[1] == jogador and velha1[4] == jogador and velha1[7] == jogador :
            return 1
    elif velha1[2] == jogador and velha1[5] == jogador and velha1[8] == jogador :
            return 1
    elif velha1[0] == jogador and velha1[4] == jogador and velha1[8] == jogador :
            return 1
    elif velha1[2] == jogador and velha1[4] == jogador and velha1[6] == jogador :
            return 1
    else:
        return 0

velha  = [] #cria a lista vazia
velha1 = [] #cria a lista vazia

continuaJogo = 'S'
getch = get._Getch() #Cria uma instância GetWindows

while continuaJogo == 'S':
    contador = 0
    DeuVelha = False
    velha = [7,8,9,4,5,6,1,2,3]
    velha1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    mostraVelha()  #inicia mostrando a grade e instruções
    while contador < 9:

        while True: #ENQUANTO FOR DIGITADO 0, VAI CONTINUAR PERGUNTANDO
            print ("\nEntre com a posição X no jogo: \n")
            pos_X = int (getch())  #executa ENTER assim que digitar
            if pos_X != 0: #SE FOR DIGITADO DIFERENTE DE 0, CONVERTE E SAI DO LAÇO
                posicao = converte(pos_X) #converte a posição
                break
            else:
                clear();
                mostraVelha()

        while True:
            if verificaPosicao(posicao) == 1:  #verifica se a posição escolhida já está ocupada
                velha1[posicao] = 'X'  # Add X na posicao informada
                contador +=1
                ganhou = verificaGanhador('X')
                break
            else:  #caso esteja, faça isso
                print ("\nPOSIÇÃO JÁ OCUPADA! Tente outra para o X: \n")
                pos_X = int (getch())   #executa ENTER assim que digitar
                posicao = converte(pos_X)

        mostraVelha()    #chama mostraVelha() para atualizar jogada na tela
        print(contador)

        if ganhou == 1:  # só sai do loop(Ganha jogo) se for igual a 1
            print('\nParabéns! o X é o vencedor!\n')
            break

        if contador == 9:  #Se houver 9 jogadas e não houver vencedor, dá Velha e a partida é encerrada
            DeuVelha = True
            break

        while True:  #ENQUANTO FOR DIGITADO 0, VAI CONTINUAR PERGUNTANDO
            print ("\nEntre com a posição O no jogo: \n")
            pos_O = int (getch())
            if pos_O != 0:  #SE FOR DIGITADO DIFERENTE DE 0, CONVERTE E SAI DO LAÇO
                posicao = converte(pos_O)
                break
            else:
                clear();
                mostraVelha()

        while True:
            if verificaPosicao(posicao) == 1:
                velha1[posicao] = 'O' # Add O na posicao informada
                contador +=1
                ganhou = verificaGanhador('O')
                break
            else:
                #pos_o = int(input('\nDigite uma posição livre para o O: \n'))
                print ("\nPOSIÇÃO JÁ OCUPADA! Tente outra para a O: \n")
                pos_O = int (getch())
                posicao = converte(pos_O)

        #velha1[posicao] = 'O'  # Add O na posicao informada
        mostraVelha()          # Chama mostraVelha() para atualizar jogada na tela
        print(contador)

        if ganhou == 1:  # só sai do loop(Ganha jogo) se for igual a 1
            print('\nParabéns! o O é o vencedor!\n')
            break

    if DeuVelha == True:
        print('\nDEU VELHA! Não houve ganhadores!\n')

    continua = input('DESEJA JOGAR OUTRA PARTIDA? -  S/N \n')
    continuaJogo = continua.upper()
