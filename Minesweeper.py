import random,time,replit

replit.clear()
def matriz_completa():

    #faz a tela de apresentação
    print()
    print("==========================================================")
    print("                  \033[1;31m~CAMPO MINADO  V.1.0~\033[m   ")
    print("==========================================================")
    print()
    inicio = input("Pressione 'I' para ver as regras do jogo,ou\nqualquer outra tecla para iniciar a partida.").upper()
    if inicio == 'I':
        replit.clear()
        print(open('regras.txt', 'r').read())
        print()
        print()
        input('\033[1;33m~Pressione qualquer tecla para jogar.\033[m ')   
    
    matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    #coloca as bombas na matriz com uma função,o range define quantas
    #bombas iram ter
    for repetir in range(15):
        colocar_bombas(matriz)
    numeros_na_tabela(matriz)

    replit.clear()
    return matriz


def colocar_bombas(matriz):
    lin = random.randint(0, 8)
    col = random.randint(0, 8)
    linha_atual = matriz[lin]
    if not linha_atual[col] == "*":
        linha_atual[col] = "*"
    else:
        colocar_bombas(matriz)

#coloca os numeros ao redor das bombas
def numeros_na_tabela(matriz):
    for i in range(9):
        for j in range(9):
            cont = 0
            if matriz[i][j] == "*":
                continue
            else:

                if ((i == 0 and j == 0) or (i == 8 and j == 0)):
                    if i == 0:
                        if matriz[i + 1][j] == "*":
                            cont += 1
                        if matriz[i + 1][j + 1] == "*":
                            cont += 1
                    else:
                        if matriz[i - 1][j] == "*":
                            cont += 1
                        if matriz[i - 1][j + 1] == "*":
                            cont += 1

                    if matriz[i][j + 1] == "*":
                        cont += 1

                    matriz[i][j] = cont
                    cont = 0

                elif (i == 0 and j == 8) or (i == 8 and j == 8):
                    if i == 0:
                        if matriz[i + 1][j] == "*":
                            cont += 1
                        if matriz[i + 1][j - 1] == "*":
                            cont += 1
                    else:
                        if matriz[i - 1][j] == "*":
                            cont += 1
                        if matriz[i - 1][j - 1] == "*":
                            cont += 1

                    if matriz[i][j - 1] == "*":
                        cont += 1

                    matriz[i][j] = cont
                    cont = 0

                elif (i == 0 or i == 8) and (j != 0 and j != 8):
                    if i == 0:
                        if matriz[i + 1][j] == "*":
                            cont += 1
                        if matriz[i + 1][j + 1] == "*":
                            cont += 1
                        if matriz[i + 1][j - 1] == "*":
                            cont += 1

                    else:
                        if matriz[i - 1][j] == "*":
                            cont += 1
                        if matriz[i - 1][j + 1] == "*":
                            cont += 1
                        if matriz[i - 1][j - 1] == "*":
                            cont += 1

                    if matriz[i][j + 1] == "*":
                        cont += 1
                    if matriz[i][j - 1] == "*":
                        cont += 1

                    matriz[i][j] = cont
                    cont = 0

                elif (j == 0 or j == 8) and (i != 0 and i != 8):
                    if j == 0:
                        if matriz[i][j + 1] == "*":
                            cont += 1
                        if matriz[i + 1][j + 1] == "*":
                            cont += 1
                        if matriz[i - 1][j + 1] == "*":
                            cont += 1
                    else:
                        if matriz[i][j - 1] == "*":
                            cont += 1
                        if matriz[i + 1][j - 1] == "*":
                            cont += 1
                        if matriz[i - 1][j - 1] == "*":
                            cont += 1

                    if matriz[i + 1][j] == "*":
                        cont += 1
                    if matriz[i - 1][j] == "*":
                        cont += 1

                    matriz[i][j] = cont
                    cont = 0

                elif (0 != i != 8) and (0 != j != 8):
                    if matriz[i + 1][j] == "*":
                        cont += 1
                    if matriz[i - 1][j] == "*":
                        cont += 1
                    if matriz[i][j + 1] == "*":
                        cont += 1
                    if matriz[i][j - 1] == "*":
                        cont += 1
                    if matriz[i + 1][j - 1] == "*":
                        cont += 1
                    if matriz[i - 1][j - 1] == "*":
                        cont += 1
                    if matriz[i + 1][j + 1] == "*":
                        cont += 1
                    if matriz[i - 1][j + 1] == "*":
                        cont += 1

                    matriz[i][j] = cont
                    cont = 0

#localiza as posição de qualquer matriz
def localizar(lin, col, matriz):
    local = matriz[lin][col]
    return local


#imprimir a matriz de forma rapida
def printar_matriz(matriz):
    for a in range(2):
        print()
    print('     A     B     C     D     E     F     G     H     I')
    print('  ╔═════╦═════╦═════╦═════╦═════╦═════╦═════╦═════╦═════╗')
    for numero in range(0, 9):
        print(numero + 1, '║ ', localizar(numero, 0, matriz), ' ║ ', localizar(numero, 1, matriz), ' ║ ',localizar(numero, 2, matriz), ' ║ ',
                                localizar(numero, 3, matriz), ' ║ ', localizar(numero, 4, matriz), ' ║ ', localizar(numero, 5, matriz),' ║ ',
                                localizar(numero, 6, matriz), ' ║ ', localizar(numero, 7, matriz), ' ║ ', localizar(numero, 8, matriz),' ║ ')

        if numero != 8:
            print('  ╠═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╣')

    print('  ╚═════╩═════╩═════╩═════╩═════╩═════╩═════╩═════╩═════╝')

    return


replit.clear()
matriz_demonstracao = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

#inicio do jogo
matriz = matriz_completa()

#Numero de espaço livres(a pessoa ganha o jogo quando todos os espaços livres são preenchidos)
espaco_vazio = 0
for i in range(9):
    for j in range(9):
        if matriz[i][j] != "*":
            espaco_vazio += 1

#funcionamento
conta_de_acertos = 0
while True:
    print()
    print("                  \033[1;31m~CAMPO MINADO  V.1.0~\033[m   ")
    printar_matriz(matriz_demonstracao)
    try:
        #caso ele ganhe o jogo:
        if conta_de_acertos == espaco_vazio:
            replit.clear()
            print("   ======================================================")
            print("   \033[1;7;37m                   VOCÊ CONSEGUIU !!                  \033[m ")
            print("   ======================================================")
            print()
            print("                    \033[46m  ~~~~PARABENS~~~~  \033[m                   ")
            print()
            printar_matriz(matriz)
            break
        print()
        print()
        #colocando bandeiras ou abrindo coordenadas
        opcoes = input("Escolha entre Coordenadas (C / c) ou Bandeira (B / b): ").lower()
        if opcoes == "b":
            lin = int(input("Linha ?"))
            col = input("Coluna ?").lower()
            col = (ord(col)) - 97
            matriz_demonstracao[lin - 1][col] = '⚐'
            replit.clear()
            time.sleep(0.50)

        elif opcoes == "c":
            lin = int(input("Linha ?"))
            col = input("Coluna ?").lower()
            lin = lin - 1
            col = (ord(col)) - 97
            #Caso a posição escolhida por ele tenha uma boma
            if matriz[lin][col] == "*":
                replit.clear()
                print("   ======================================================")
                print("   \033[1;7;37m                   VOCÊ PERDEU !!                     \033[m ")
                print("   ======================================================")
                print()
                print("           \033[46m  ~~~~MAIS SORTE NA PROXIMA VEZ~~~~  \033[m                   ")
                print()
                printar_matriz(matriz)
                break
            #caso nao tenha(a matriz demonstração na posição escolhida assumi o valor da matriz principal e em seguida ele tem um contador de numeros de espaços vazios q ele conseguiu com sucesso)
            else:
                matriz_demonstracao[lin][col] = matriz[lin][col]
                conta_de_acertos += 1
                replit.clear()
                time.sleep(0.40)

        #caso ele nao ensira o valor correto
        elif opcoes != "b" or opcoes != "c":
            replit.clear()
            print()
            print()
            print("ERRO 404 - NOT FOUND")
            print("INSIRA VALORES VÁLIDOS !!!")
            print()
            replit.clear()
            time.sleep(1.10)

    #caso ele coloque algum dado sem ligação ao jogo
    except:
        replit.clear()
        print()
        print()
        print("ERRO 404 - NOT FOUND")
        print("INSIRA VALORES VÁLIDOS !!!")
        print()
        replit.clear()
        time.sleep(1.10)
