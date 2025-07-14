import os
import random
from palavras import palavras_facil, palavras_medio, palavras_dificil, palavras_expert



def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


limpar_terminal()
print("Seja bem-vind@ ao clássico Jogo da Forca! 😀\n")
print("A sua missão é descobrir qual é a palavra secreta testando uma letra por vez.")
print("Mas cuidado! Suas tentativas são limitadas.")
print("Se você testar uma letra que não está na palavra, você perde uma tentativa. Se suas tentativas zerarem, você perde o jogo.\n")
print("\tImportante: neste jogo, caracteres similares, como A e À ou C e Ç, NÃO serão considerados iguais.\n")


def jogo_da_forca():
    tentativas = ""
    letras_descobertas = []
    letras_erradas = []
        
    palavra, dica = "", "?"
    
    def selecionar_dificuldade():
        print("Antes de começarmos, preciso que você escolha uma dificuldade para o jogo:\n")
        print("\t(F)ácil: 6 tentativas; palavras simples; com dica.")
        print("\t(M)édio: 5 tentativas; palavras não tão comuns; com dica.")
        print("\t(D)ifícil: 4 tentativas; palavras muito incomuns; com dica.")
        print("\t(E)xpert: 4 tentativas; palavras complexas; dica semioculta.\n")
        dificuldade = input("Dificuldade? ").upper()

        if dificuldade == "F":
            limpar_terminal()
            return 6, *random.choice(list(palavras_facil.items())), "Fácil"
        
        elif dificuldade == "M":
            limpar_terminal()
            return 5, *random.choice(list(palavras_medio.items())), "Médio"
        
        elif dificuldade == "D":
            limpar_terminal()
            return 4, *random.choice(list(palavras_dificil.items())), "Difícil"
        
        elif dificuldade == "E":
            limpar_terminal()
            palavra, dica = random.choice(list(palavras_expert.items()))
            return 4, palavra, (dica[0] + "?" * (len(dica) - 1)), "Expert"
        
        else:
            limpar_terminal()
            print("Opção inválida. Tente novamente.\n")
            return selecionar_dificuldade()
    
    
    
    tentativas, palavra, dica, dificuldade = selecionar_dificuldade()
    
    
    
    for letra in palavra:
        if letra != " ":
            letras_descobertas.append("_")
        
        else:
            letras_descobertas.append(" ")
    
    
    def status():
        print(f"Dica: {dica}", end="     ")
        print(f"Tentativas restantes: {tentativas}", end="     ")
        print(f"Dificuldade: {dificuldade}", end="     ")
        print(f"Letras erradas: {letras_erradas}\n")
        print("\t", end="")
        for letra in letras_descobertas:    
            print(letra, end=" ")

        print("\n")

    
    while True:
        
        status()
        tentativa = input("Tentativa? ").upper()
        
        if tentativa in letras_descobertas or tentativa in letras_erradas:
            limpar_terminal()
            print("🟡 Essa letra já foi dita. Tente outra letra.\n")
            continue
        
        if len(tentativa) > 1 or not tentativa.isalpha():
            limpar_terminal()
            print("🟡 Esse não é um caractere válido. Tente novamente.\n")
            continue
        
        
        if tentativa in palavra:
            for i in range(len(palavra)):
                if palavra[i] == tentativa:
                    letras_descobertas[i] = tentativa
            
            limpar_terminal()
            print("✅ Letra certa! :)\n")
        
        else:
            tentativas -= 1
            limpar_terminal()
            print("❌ Letra errada... :(\n")
            letras_erradas.append(tentativa)
        
        
        if not "_" in letras_descobertas:
            limpar_terminal()
            print("Você venceu! Parabéns! 🥳")
            print(f"A palavra era: {palavra}\n")
            break
            
        elif tentativas == 0:
            limpar_terminal()
            print("Infelizmente, você perdeu... 😔")
            print(f"A palavra era: {palavra}\n")
            break
        
    jogarNovamente = input("Jogar novamente (s/n)? ")
    
    if jogarNovamente == "s":
        limpar_terminal()
        jogo_da_forca()
    else:
        limpar_terminal()
        return "Programa encerrado."

jogo_da_forca()