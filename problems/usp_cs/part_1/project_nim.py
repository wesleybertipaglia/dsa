def computador_escolhe_jogada(n, m):
    if n % (m + 1) == 0:
        return m
    else:
        return n % (m + 1)

def usuario_escolhe_jogada(n, m):
    while True:
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada >= 1 and jogada <= m and jogada <= n:
            return jogada
        else:
            print("Oops! Jogada inválida! Tente de novo.")

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    
    if n % (m + 1) == 0:
        print("Você começa!")
        turno = "usuario"
    else:
        print("Computador começa!")
        turno = "computador"
    
    while n > 0:
        if turno == "usuario":
            jogada = usuario_escolhe_jogada(n, m)
            turno = "computador"
        else:
            jogada = computador_escolhe_jogada(n, m)
            turno = "usuario"
        
        n -= jogada
        print(f"Agora restam {n} peças no tabuleiro.")
        
        if n == 0:
            if turno == "usuario":
                print("O computador ganhou!")
                return "O computador ganhou!"
            else:
                print("Você ganhou!")
                return "Você ganhou!"

def campeonato():
    placar_usuario = 0
    placar_computador = 0
    
    for rodada in range(1, 4):
        print(f"**** Rodada {rodada} ****")
        resultado = partida()
        
        if "Você ganhou!" in resultado:
            placar_usuario += 1
        else:
            placar_computador += 1
    
    print("**** Final do campeonato! ****")
    print(f"Placar: Você {placar_usuario} X {placar_computador} Computador")

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    
    escolha = int(input())
    
    if escolha == 1:
        partida()
    elif escolha == 2:
        campeonato()

if __name__ == "__main__":
    main()
