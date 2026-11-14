total_partidas, vitorias_X, vitorias_O, empates = 0, 0, 0, 0
seq_X, seq_O, max_seq_X, max_seq_O = 0, 0, 0, 0
tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
executando = True

while executando == True:
    print("\n=== JOGO DA VELHA ===")
    print("1. Jogar\n2. Sair")
    opcao = input("Escolha uma opção: ")

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
