from colorama import Fore, Style

def menu():
        continuar = 1
        banner()
        
        while continuar:
                continuar = int(input("0: sair \n" + "1: jogar novamente \n"))
                if continuar:
                        game()
                else:
                    print("Saindo... ")
def banner():
      art = """
                     #      ##       ###      ##              ####       ##              #    #   ######   #        #    #     ##
           #  #     #   #    #  #              #  #     #  #             #    #   #        #        #    #    #  #
    ##    #    #   #        #    #             #   #   #    #            #    #   #        #        #    #   #    #
     #    #    #   #  ###   #    #             #   #   ######             #  #    ####     #        ######   ######
     #    #    #   #    #   #    #             #   #   #    #             #  #    #        #        #    #   #    #
     #     #  #     #   #    #  #              #  #    #    #              ##     #        #        #    #   #    #
 #   #      ##       ###      ##              ####     #    #              ##     ######   ######   #    #   #    #
  ###


"""     
      print(f"{Fore.RED}{art}{Style.RESET_ALL}")
def game():
    res = int(input("1: quero ser X\n" + "2: quero ser O \n"))
    if res == 1:
          jogada = 2
    else:
        jogada = 1
    while ganhou() == 0:
        if jogada % 2 + 1 == 1:
            print("\nJogador X")
        else:
            print("\nJogador O")
        
        tabuleiro()

        linha = int(input("\nLinha: "))
        coluna = int(input("Coluna: "))

        if linha not in {1, 2, 3} or coluna not in {1, 2, 3}:
            print("Linha ou coluna inválida\n")
        elif board[linha - 1][coluna - 1] == 0:
            if (jogada % 2 + 1) == 1:
                board[linha - 1][coluna - 1] = 1
            else:
                board[linha - 1][coluna - 1] = -1
            jogada += 1  # Incrementa jogada apenas se a jogada foi bem-sucedida
        else:
            print("Posição não está vazia")

        if ganhou():
            print("Jogador ", jogada % 2 + 1, " ganhou após ", jogada + 1, " rodadas")

    

def ganhou():
       for i in range(3):
               soma = board[i][0]+board[i][1]+board[i][2]
               if soma==3 or soma ==-3:
                    return 1
          #checando colunas
       for i in range(3):
            soma = board[0][i]+board[1][i]+board[2][i]
            if soma==3 or soma ==-3:
                return 1

        #checando diagonais
       diagonal1 = board[0][0]+board[1][1]+board[2][2]
       diagonal2 = board[0][2]+board[1][1]+board[2][0]
       if diagonal1==3 or diagonal1==-3 or diagonal2==3 or diagonal2==-3:
            return 1

       return 0

def tabuleiro():
       for i in range(3):
              for j in range(3):
                     if board[i][j] == 0:
                            print("_", end='')
                     elif board[i][j] == 1:
                            print("x", end='')
                     elif board[i][j] == -1:
                            print("o", end='')
              print()
                     

board= [ [0,0,0],
         [0,0,0],
         [0,0,0] ]
menu()