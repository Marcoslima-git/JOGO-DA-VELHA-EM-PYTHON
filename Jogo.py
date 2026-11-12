total_partidas, vitorias_X, vitorias_O, empates = 0, 0, 0, 0
seq_X, seq_O, max_seq_X, max_seq_O = 0, 0, 0, 0

tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
executando = True

# Menu Principal controlado por while
while executando == True:
    print("\n=== JOGO DA VELHA ===")
    print("1. Jogar")
    print("2. Ver regras")
    print("3. Ver placar")
    print("4. Sair")

    opcao = input("Escolha uma opção (1 a 4): ")
linha_str + tabuleiro[i][j] + " "
                print(linha_str)
            print("\nVez do jogador", turno)

            # Validação de entradas (Anti-Crash sem try/except e sem isdigit)
            jogada_valida = False
            while jogada_valida == False:
                entrada_l = input("Digite a linha (1 a 3): ")
                entrada_c = input("Digite a coluna (1 a 3): ")

                linha_ok = False
                coluna_ok = False
                l_idx = 0
                c_idx = 0

                # Comparação com opções válidas convertidas em string usando laço for
                for n in range(1, 4):
                    if entrada_l == str(n):
                        linha_ok = True
                        l_idx = n - 1
                    if entrada_c == str(n):
                        coluna_ok = True
                        c_idx = n - 1
                jogada_valida = True # trava temporária
            jogo_ativo = False
