#Configuração do Tabuleiro
def criar_tabuleiro():
    return [[' ' for _ in range(3)] for _ in range(3)]

#Exibição do Tabuleiro
def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)

#Verificação de Condições de Vitória
def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if all([c == jogador for c in linha]):
            return True

    # Verificar colunas
    for col in range(3):
        if all([tabuleiro[linha][col] == jogador for linha in range(3)]):
            return True

    # Verificar diagonais
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or all([tabuleiro[i][2-i] == jogador for i in range(3)]):
        return True

    return False

#Movimentos dos Jogadores
def movimento_valido(tabuleiro, linha, coluna):
    return tabuleiro[linha][coluna] == ' '

def fazer_movimento(tabuleiro, linha, coluna, jogador):
    if movimento_valido(tabuleiro, linha, coluna):
        tabuleiro[linha][coluna] = jogador
        return True
    return False

#Loop do Jogo Principal
def jogo_da_velha():
    tabuleiro = criar_tabuleiro()
    jogador_atual = 'X'
    jogadas = 0

    while jogadas < 9:
        exibir_tabuleiro(tabuleiro)
        try:
            linha = int(input(f"Jogador {jogador_atual}, digite a linha (0-2): "))
            coluna = int(input(f"Jogador {jogador_atual}, digite a coluna (0-2): "))
            
            if linha not in range(3) or coluna not in range(3):
                print("Posição inválida! Tente novamente.")
                continue

            if fazer_movimento(tabuleiro, linha, coluna, jogador_atual):
                if verificar_vitoria(tabuleiro, jogador_atual):
                    exibir_tabuleiro(tabuleiro)
                    print(f"Jogador {jogador_atual} venceu!")
                    return
                jogador_atual = 'O' if jogador_atual == 'X' else 'X'
                jogadas += 1
            else:
                print("Movimento inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida! Por favor, digite números inteiros entre 0 e 2.")

    exibir_tabuleiro(tabuleiro)
    print("Empate!")

# Executar o jogo
jogo_da_velha()
 