partidas = 0
acertosPartidas = 0
melhorPontuacao = 0
jogar = "sim"

print("Deseja começar o jogo?: ")
deseja = input()
if deseja == "sim":

    while jogar == "sim":
        partidas += 1
        acertos = 0

        print("PARTIDA", partidas)

        print("1) Qual é a capital do Brasil?")
        print("A) Rio de Janeiro")
        print("B) Brasília")
        print("C) São Paulo")
        resposta = input("Resposta: ").upper()

        if resposta == "B":
            acertos += 1
            print("Você acertou!!")
        else:
            print("Resposta incorreta. Resposta certa: B")

        print("2) Quanto é 5 x 4?")
        print("A) 20")
        print("B) 15")
        print("C) 25")
        resposta = input("Resposta: ").upper()

        if resposta == "A":
            acertos += 1
            print("Você acertou!!")
        else:
            print("Resposta incorreta. Resposta certa: A")

        print("3) Qual é o menor país do mundo?")
        print("A) Argentina")
        print("B) Chile")
        print("C) Vaticano")
        resposta = input("Resposta: ").upper()

        if resposta == "C":
            acertos += 1
            print("Você acertou!!")
        else:
            print("Resposta incorreta. Resposta certa: C")

        print("4) Quantos dias há em uma semana?")
        print("A) 5")
        print("B) 7")
        print("C) 10")
        resposta = input("Resposta: ").upper()

        if resposta == "B":
            acertos += 1
            print("Você acertou!!")
        else:
            print("Resposta incorreta. Resposta certa: B")

        print("5) Qual planeta é conhecido como Planeta Vermelho?")
        print("A) Marte")
        print("B) Júpiter")
        print("C) Saturno")
        resposta = input("Resposta: ").upper()

        if resposta == "A":
            acertos += 1
            print("Você acertou!!")
        else:
            print("Resposta incorreta. Resposta certa: A")

        print("Você acertou", acertos, "de 5 perguntas.")

        acertosPartidas += acertos

        if acertos > melhorPontuacao:
            melhorPontuacao = acertos

        jogar = input("Deseja jogar novamente? (sim ou não): ").lower()

        if jogar == "sim":
            print("Iniciando uma nova partida...")
            
        elif jogar == "não":
            print("RESULTADO:")
            print("Total de partidas: ", partidas)
            print("Total de pontos: ", acertosPartidas)
            print("Melhor partida: ", melhorPontuacao)
            print("Média de acertos por partida: ", acertosPartidas / partidas)
            print("Fim do jogo!")
