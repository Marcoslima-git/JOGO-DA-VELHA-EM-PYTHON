total_partidas, vitorias_X, vitorias_O, empates = 0, 0, 0, 0
seq_X, seq_O, max_seq_X, max_seq_O = 0, 0, 0, 0
tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
executando = True

while executando == True:
    print("\n=== JOGO DA VELHA ===")
    print("1. Jogar\n2. Ver regras\n3. Ver placar\n4. Sair")
    opcao = input("Escolha uma opção (1 a 4): ")

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
            print("\nVez do jogador", turno)

            jogada_valida = False
            while jogada_valida == False:
                entrada_l = input("Digite a linha (1 a 3): ")
                entrada_c = input("Digite a coluna (1 a 3): ")
                linha_ok, coluna_ok, l_idx, c_idx = False, False, 0, 0
                for n in range(1, 4):
                    if entrada_l == str(n): linha_ok, l_idx = True, n - 1
                    if entrada_c == str(n): coluna_ok, c_idx = True, n - 1
                if linha_ok == True and coluna_ok == True:
                    if tabuleiro[l_idx][c_idx] == " ": jogada_valida = True
                    else: print("Casa ocupada! Tente novamente.")
                else: print("Entrada inválida! Digite apenas números de 1 a 3.")

            tabuleiro[l_idx][c_idx] = turno

            # Verificação de vitória com laços for
            venceu = False
            # Verificando Linhas
            for i in range(3):
                if tabuleiro[i][0] == turno and tabuleiro[i][1] == turno and tabuleiro[i][2] == turno:
                    venceu = True
            # Verificando Colunas
            for j in range(3):
                if tabuleiro[0][j] == turno and tabuleiro[1][j] == turno and tabuleiro[2][j] == turno:
                    venceu = True
            jogo_ativo = False
