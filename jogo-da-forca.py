import os
import random
from palavras import palavras

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def jogo_da_forca():
    tentativas = 5
    letras_descobertas = []
    letras_erradas = []

    
    
    palavra, dica = random.choice(list(palavras.items()))
    
    for letra in palavra:
        if letra != " ":
            letras_descobertas.append("_")
        
        else:
            letras_descobertas.append(" ")
    
    
    def status():
        print(f"Dica: {dica}", end="     ")
        print(f"Letras erradas: {letras_erradas}", end="     ")
        print(f"Tentativas restantes: {tentativas}\n")
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
            print(f"A palavra era: {palavra}")
            break
            
        elif tentativas == 0:
            limpar_terminal()
            print("Infelizmente, você perdeu... 😔")
            print(f"A palavra era: {palavra}")
            break

jogo_da_forca()