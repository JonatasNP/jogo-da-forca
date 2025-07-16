import os
import random
from palavras import palavras_facil, palavras_medio, palavras_dificil, palavras_expert


banco_facil = palavras_facil.copy()
banco_medio = palavras_medio.copy()
banco_dificil = palavras_dificil.copy()
banco_expert = palavras_expert.copy()




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
        print("\t(F)ácil: 6 tentativas; palavras simples; dica simples.")
        print("\t(M)édio: 5 tentativas; palavras não tão comuns; dica simples.")
        print("\t(D)ifícil: 4 tentativas; palavras muito incomuns; dica simples; um caractere fica bloqueado.")
        print("\t(E)xpert: 4 tentativas; palavras complexas; dica simples; dois caracteres ficam bloqueados!\n")
        dificuldade = input("Dificuldade? ").upper()

        if dificuldade == "F":
            if not banco_facil:
                limpar_terminal()
                print("Não há mais palavras disponíveis nesta dificuldade. ⚠️")
                return selecionar_dificuldade()
            palavra, dica = random.choice(list(banco_facil.items()))
            del banco_facil[palavra]
            limpar_terminal()
            return 6, palavra, dica, "Fácil"
        
        elif dificuldade == "M":
            if not banco_medio:
                limpar_terminal()
                print("Não há mais palavras disponíveis nesta dificuldade. ⚠️")
                return selecionar_dificuldade()
            palavra, dica = random.choice(list(banco_medio.items()))
            del banco_medio[palavra]
            limpar_terminal()
            return 5, palavra, dica, "Médio"
        
        elif dificuldade == "D":
            if not banco_dificil:
                limpar_terminal()
                print("Não há mais palavras disponíveis nesta dificuldade. ⚠️")
                return selecionar_dificuldade()
            palavra, dica = random.choice(list(banco_dificil.items()))
            del banco_dificil[palavra]
            limpar_terminal()
            return 4, palavra, dica, "Difícil"
        
        elif dificuldade == "E":
            if not banco_expert:
                limpar_terminal()
                print("Não há mais palavras disponíveis nesta dificuldade. ⚠️")
                return selecionar_dificuldade()
            palavra, dica = random.choice(list(banco_expert.items()))
            del banco_expert[palavra]
            limpar_terminal()
            dica_modificada = dica       # MODIFICAR NO FUTURO
            return 4, palavra, dica_modificada, "Expert"
        
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
    
    
    # EXPERT - Bloquear um caractere ------------ ISSUE: o caractere bloqueado pode ser um espaço em branco. (Corrigir!)
    if dificuldade == "Difícil":
        bloq1 = random.randint(0, len(palavra) - 1)
        letras_descobertas[bloq1] = "🔒"
    elif dificuldade == "Expert":
        bloq1 = random.randint(0, len(palavra) - 1)
        bloq2 = random.randint(0, len(palavra) - 1)
        while bloq1 == bloq2:
            bloq2 = random.randint(0, len(palavra) - 1)
        letras_descobertas[bloq1] = "🔒"
        letras_descobertas[bloq2] = "🔒"
    
    
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
                if palavra[i] == tentativa and letras_descobertas[i] != "🔒":
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
            percentual_acertos = len(letras_descobertas) * 100 / len(palavra)
            limpar_terminal()
            print("Infelizmente, você perdeu... 😔")
            print(f"A palavra era: {palavra}\n")
            print(f"{percentual_acertos:.1f}% da palavra foi descoberta.")
            break
        
    jogarNovamente = input("Jogar novamente (s/n)? ")
    
    if jogarNovamente == "s":
        limpar_terminal()
        jogo_da_forca()
    else:
        limpar_terminal()
        return "Programa encerrado."

jogo_da_forca()