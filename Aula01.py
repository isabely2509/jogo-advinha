print("Osvaldo Cruz")

def jogo_advinhacao():
    numero_secreto = random.raidint(1, 100)
    tentativas = 0

    print("Bem Vindo ao jogo de advinhação")
    print("Estou pensando em um numero de 1 a 100")

    while True:
        try:
            palpite = int(input("Digite seu palpite"))
            tentativas += 1

            if palpite < numero_secreto:
               print("Muito baixo")
            elif palpite > numero_secreto:
               print("Muito alto")
            else:
                print("Parabens você advinhou o número em (tentavivas) tentativas")
                break
            except ValueError
                print("Por favor digite um numero valido")
            
if_name_ == "__main__"
    jogo_advinhacao()