total_partidas, vitorias_X, vitorias_O, empates = 0, 0, 0, 0
seq_X, seq_O, max_seq_X, max_seq_O = 0, 0, 0, 0
tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
executando = True

while executando == True:
    print("\n=== JOGO DA VELHA ===")
    print("1. Jogar\n2. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        for i in range(3):
            for j in range(3): tabuleiro[i][j] = " "
        turno = "X"
        jogo_ativo = True

        while jogo_ativo == True:
            print("\n  1 2 3")
            for i in range(3):
                linha_str = str(i + 1) + " "
                for j in range(3): linha_str = linha_str + tabuleiro[i][j] + " "
                print(linha_str)

            jogada_valida = False
            while jogada_valida == False:
                entrada_l = input("Linha (1 a 3): ")
                entrada_c = input("Coluna (1 a 3): ")
                linha_ok, coluna_ok, l_idx, c_idx = False, False, 0, 0
                for n in range(1, 4):
                    if entrada_l == str(n): linha_ok, l_idx = True, n - 1
                    if entrada_c == str(n): coluna_ok, c_idx = True, n - 1
                if linha_ok == True and coluna_ok == True:
                    if tabuleiro[l_idx][c_idx] == " ": jogada_valida = True
                    else: print("Casa ocupada!")
                else: print("Entrada inválida!")

            tabuleiro[l_idx][c_idx] = turno
            venceu = False
            for i in range(3):
                if tabuleiro[i][0] == turno and tabuleiro[i][1] == turno and tabuleiro[i][2] == turno: venceu = True
            for j in range(3):
                if tabuleiro[0][j] == turno and tabuleiro[1][j] == turno and tabuleiro[2][j] == turno: venceu = True
            cont_dp, cont_ds = 0, 0
            for i in range(3):
                if tabuleiro[i][i] == turno: cont_dp = cont_dp + 1
                for j in range(3):
                    if i + j == 2 and tabuleiro[i][j] == turno: cont_ds = cont_ds + 1
            if cont_dp == 3 or cont_ds == 3: venceu = True

            vazias = 0
            for i in range(3):
                for j in range(3):
                    if tabuleiro[i][j] == " ": vazias = vazias + 1

            if venceu == True:
                print("\nParabéns! O jogador", turno, "venceu!")
                total_partidas = total_partidas + 1
                if turno == "X":
                    vitorias_X = vitorias_X + 1
                    seq_X = seq_X + 1
                    seq_O = 0
                    if seq_X > max_seq_X: max_seq_X = seq_X
                else:
                    vitorias_O = vitorias_O + 1
                    seq_O = seq_O + 1
                    seq_X = 0
                    if seq_O > max_seq_O: max_seq_O = seq_O
                jogo_ativo = False
            elif vazias == 0:
                print("\nDeu empate!")
                empates = empates + 1
                total_partidas = total_partidas + 1
                seq_X, seq_O = 0, 0
                jogo_ativo = False
            else:
                if turno == "X": turno = "O"
                else: turno = "X"

elif opcao == "2":
        print("\n--- REGRAS ---")
        print("1. O jogo ocorre num tabuleiro de 3x3.")
        print("2. Vence quem completar primeiro linha, coluna ou diagonal.")
        print("3. Se o tabuleiro encher, é empate.")

    elif opcao == "3":
        print("\n--- PLACAR ACUMULADO ---")
        print("Vitórias X:", vitorias_X)
        print("Vitórias O:", vitorias_O)
        print("Total de empates:", empates)

elif opcao == "4":
        print("\n=== ESTATÍSTICAS FINAIS DA SESSÃO ===")
        print("Total de partidas jogadas:", total_partidas)
        print("Vitórias X:", vitorias_X)
        print("Vitórias O:", vitorias_O)
        print("Empates:", empates)
        executando = False
# Variáveis para estatísticas (Desafio: Estatísticas da Sessão)
total_partidas = 0
vitorias_X = 0
vitorias_O = 0
empates = 0
seq_X = 0
seq_O = 0
max_seq_X = 0
max_seq_O = 0

# Matriz do tabuleiro
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

executando = True
while executando == True:
    print("\n=== JOGO DA VELHA ===")
    print("1. Jogar")
    print("2. Ver regras")
    print("3. Ver placar")
    print("4. Sair")

    opcao = input("Escolha uma opção (1 a 4): ")

    if opcao == "1":
        for i in range(3):
            for j in range(3):
                tabuleiro[i][j] = " "

        turno = "X"
        jogo_ativo = True

        while jogo_ativo == True:
            print("\n  1 2 3")
            for i in range(3):
                linha_str = str(i + 1) + " "
                for j in range(3):
                    linha_str = linha_str + tabuleiro[i][j] + " "
                print(linha_str)

            print("\nVez do jogador", turno)

            jogada_valida = False
            while jogada_valida == False:
                entrada_l = input("Digite a linha (1 a 3): ")
                entrada_c = input("Digite a coluna (1 a 3): ")

                linha_ok = False
                coluna_ok = False
                l_idx = 0
                c_idx = 0

                for n in range(1, 4):
                    if entrada_l == str(n):
                        linha_ok = True
                        l_idx = n - 1
                    if entrada_c == str(n):
                        coluna_ok = True
                        c_idx = n - 1

                if linha_ok == True and coluna_ok == True:
                    if tabuleiro[l_idx][c_idx] == " ":
                        jogada_valida = True
                    else:
                        print("Casa ocupada! Tente novamente.")
                else:
                    print("Entrada inválida! Digite apenas números de 1 a 3.")

            tabuleiro[l_idx][c_idx] = turno

            venceu = False
            for i in range(3):
                if tabuleiro[i][0] == turno and tabuleiro[i][1] == turno and tabuleiro[i][2] == turno:
                    venceu = True
            for j in range(3):
                if tabuleiro[0][j] == turno and tabuleiro[1][j] == turno and tabuleiro[2][j] == turno:
                    venceu = True
            
            cont_dp = 0
            for i in range(3):
                if tabuleiro[i][i] == turno: cont_dp = cont_dp + 1
            if cont_dp == 3: venceu = True

            cont_ds = 0
            for i in range(3):
                for j in range(3):
                    if i + j == 2:
                        if tabuleiro[i][j] == turno:
                            cont_ds = cont_ds + 1
            if cont_ds == 3: venceu = True

            vazias = 0
            for i in range(3):
                for j in range(3):
                    if tabuleiro[i][j] == " ":
                        vazias = vazias + 1

            if venceu == True:
                print("\n  1 2 3")
                for i in range(3):
                    linha_str = str(i + 1) + " "
                    for j in range(3):
                        linha_str = linha_str + tabuleiro[i][j] + " "
                    print(linha_str)
                print("\nParabéns! O jogador", turno, "venceu!")
                total_partidas = total_partidas + 1

                if turno == "X":
                    vitorias_X = vitorias_X + 1
                    seq_X = seq_X + 1
                    seq_O = 0
                    if seq_X > max_seq_X: max_seq_X = seq_X
                else:
                    vitorias_O = vitorias_O + 1
                    seq_O = seq_O + 1
                    seq_X = 0
                    if seq_O > max_seq_O: max_seq_O = seq_O
                jogo_ativo = False

            elif vazias == 0:
                print("\n  1 2 3")
                for i in range(3):
                    linha_str = str(i + 1) + " "
                    for j in range(3):
                        linha_str = linha_str + tabuleiro[i][j] + " "
                    print(linha_str)
                print("\nDeu empate!")
                empates = empates + 1
                total_partidas = total_partidas + 1
                seq_X = 0
                seq_O = 0
                jogo_ativo = False
            else:
                if turno == "X": turno = "O"
                else: turno = "X"

    elif opcao == "2":
        print("\n--- REGRAS ---")
        print("1. O jogo ocorre num tabuleiro de 3 linhas e 3 colunas.")
        print("2. Os dois jogadores se alternam marcando X ou O em casas vazias.")
        print("3. Vence quem completar primeiro uma linha, coluna ou diagonal com seu símbolo.")
        print("4. Se o tabuleiro encher sem vencedor, é empate.")

    elif opcao == "3":
        print("\n--- PLACAR ACUMULADO ---")
        print("Vitórias do jogador X:", vitorias_X)
        print("Vitórias do jogador O:", vitorias_O)
        print("Total de empates:", empates)

    elif opcao == "4":
        print("\n=== ESTATÍSTICAS FINAIS DA SESSÃO ===")
        print("Total de partidas jogadas:", total_partidas)
        print("Vitórias X:", vitorias_X)
        print("Vitórias O:", vitorias_O)
        print("Empates:", empates)

        if total_partidas > 0:
            perc_X = (vitorias_X * 100.0) / total_partidas
            perc_O = (vitorias_O * 100.0) / total_partidas
            print("Porcentagem de vitória X:", perc_X, "%")
            print("Porcentagem de vitória O:", perc_O, "%")
        else:
            print("Nenhuma partida foi concluída para gerar a porcentagem.")

        print("Maior sequência de vitórias consecutivas de X:", max_seq_X)
        print("Maior sequência de vitórias consecutivas de O:", max_seq_O)
        print("\nSaindo do programa... Até a próxima!")
        executando = False
    else:
        print("Opção inválida! Escolha um número de 1 a 4.")
