import os
import random
from palavras import palavras_facil, palavras_medio, palavras_dificil, palavras_expert

bancos = {
    "F": palavras_facil.copy(),
    "M": palavras_medio.copy(),
    "D": palavras_dificil.copy(),
    "E": palavras_expert.copy()
}


def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_boas_vindas():
    limpar_terminal()
    print("Seja bem-vind@ ao clássico Jogo da Forca! 😀\n")
    print("A sua missão é descobrir qual é a palavra secreta testando uma letra por vez.")
    print("Mas cuidado! Suas tentativas são limitadas.")
    print("Se você testar uma letra que não está na palavra, você perde uma tentativa. Se suas tentativas zerarem, você perde o jogo.\n")
    print("\tImportante: neste jogo, caracteres similares, como A e À ou C e Ç, NÃO serão considerados iguais.\n")


def selecionar_dificuldade():
    opcoes = {
        "F": (6, "Fácil"),
        "M": (5, "Médio"),
        "D": (4, "Difícil"),
        "E": (4, "Expert")
    }
    
    while True:
        print("Escolha uma dificuldade:\n")
        print("\t(F)ácil: 6 tentativas; dica simples.")
        print("\t(M)édio: 5 tentativas; dica simples.")
        print("\t(D)ifícil: 4 tentativas; 1 caractere bloqueado.")
        print("\t(E)xpert: 4 tentativas; 2 caracteres bloqueados.\n")

        escolha = input("Dificuldade? ").upper()
        if escolha in opcoes:
            banco = bancos[escolha]
            if not banco:
                limpar_terminal()
                print("⚠️ Não há mais palavras disponíveis nesta dificuldade.\n")
            else:
                tentativas, nome_dificuldade = opcoes[escolha]
                palavra, dica = random.choice(list(banco.items()))
                del banco[palavra]
                limpar_terminal()
                return tentativas, palavra, dica, nome_dificuldade
        else:
            limpar_terminal()
            print("⚠️ Opção inválida. Tente novamente.\n")


def bloquear_caracteres(palavra, dificuldade, letras_descobertas):
    qtd_bloqueios = 0
    if dificuldade == "Difícil":
        qtd_bloqueios = 1
    elif dificuldade == "Expert":
        qtd_bloqueios = 2

    indices = random.sample([i for i in range(len(palavra)) if palavra[i] != " "], k=qtd_bloqueios)
    for i in indices:
        letras_descobertas[i] = "🔒"


def mostrar_status(dica, tentativas, dificuldade, letras_erradas, letras_descobertas):
    print(f"Dica: {dica}", end="     ")
    print(f"Tentativas restantes: {tentativas}", end="     ")
    print(f"Dificuldade: {dificuldade}", end="     ")
    print(f"Letras erradas: {letras_erradas}\n")
    print("\t", end="")
    for letra in letras_descobertas:
        print(letra, end=" ")
    print("\n")


def processar_tentativa(palavra, tentativa, letras_descobertas, letras_erradas):
    if tentativa in letras_descobertas or tentativa in letras_erradas:
        print("🟡 Essa letra já foi dita. Tente outra letra.\n")
        return None

    if len(tentativa) != 1 or not tentativa.isalpha():
        print("🟡 Esse não é um caractere válido. Tente novamente.\n")
        return None

    if tentativa in palavra:
        for i in range(len(palavra)):
            if palavra[i] == tentativa and letras_descobertas[i] == "_":
                letras_descobertas[i] = tentativa
        print("✅ Letra certa! :)\n")
        return True
    else:
        letras_erradas.append(tentativa)
        print("❌ Letra errada... :(\n")
        return False


def jogar_rodada(tentativas, palavra, dica, dificuldade):
    letras_descobertas = ["_" if letra != " " else " " for letra in palavra]
    letras_erradas = []

    bloquear_caracteres(palavra, dificuldade, letras_descobertas)

    while True:
        mostrar_status(dica, tentativas, dificuldade, letras_erradas, letras_descobertas)
        tentativa = input("Tentativa? ").upper()
        limpar_terminal()

        resultado = processar_tentativa(palavra, tentativa, letras_descobertas, letras_erradas)
        if resultado is None:
            continue
        elif not resultado:
            tentativas -= 1

        if "_" not in letras_descobertas:
            print("Você venceu! Parabéns! 🥳")
            print(f"A palavra era: {palavra}\n")
            break
        elif tentativas == 0:
            print("Infelizmente, você perdeu... 😔")
            print(f"A palavra era: {palavra}\n")
            break


def jogo_da_forca():
    mostrar_boas_vindas()

    while True:
        tentativas, palavra, dica, dificuldade = selecionar_dificuldade()
        jogar_rodada(tentativas, palavra, dica, dificuldade)

        novamente = input("Jogar novamente (s/n)? ").lower()
        if novamente != "s":
            limpar_terminal()
            print("Programa encerrado.")
            break
        
        limpar_terminal()


jogo_da_forca()