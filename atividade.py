import random

def escolher_filme():
    filmes = [
        "TITANIC",
        "MATRIX",
        "AVATAR",
        "GLADIADOR",
        "INTERESTELAR",
        "O PODEROSO CHEFAO",
        "HARRY POTTER",
        "SENHOR DOS ANEIS",
        "JURASSIC PARK",
        "DE VOLTA PARA O FUTURO"
    ]
    return random.choice(filmes)

def mostrar_palavra(palavra, letras_certas):
    exibicao = ""
    for letra in palavra:
        if letra == " ":
            exibicao += "  "
        elif letra.upper() in letras_certas:
            exibicao += letra.upper() + " "
        else:
            exibicao += "_ "
    return exibicao

def jogo():
    palavra = escolher_filme()
    letras_certas = set()
    letras_erradas = set()
    tentativas = 6

    print("🎬 Bem-vindo ao jogo de adivinhar o FILME!")
    print("Tente descobrir o nome do filme:")
    
    while tentativas > 0:
        print("\nPalavra:", mostrar_palavra(palavra, letras_certas))
        print(f"Erros ({len(letras_erradas)}): {' '.join(letras_erradas)}")
        print(f"Tentativas restantes: {tentativas}")

        chute = input("Digite uma letra: ").upper()

        if not chute.isalpha() or len(chute) != 1:
            print("Digite apenas uma letra válida!")
            continue

        if chute in letras_certas or chute in letras_erradas:
            print("Você já tentou essa letra!")
            continue

        if chute in palavra:
            letras_certas.add(chute)
            print("✔ Boa! A letra está na palavra.")
        else:
            letras_erradas.add(chute)
            tentativas -= 1
            print("✖ Letra errada.")
        
        
        if all(letra in letras_certas or letra == " " for letra in palavra):
            print("\n🎉 PARABÉNS! Você acertou o filme!")
            print("Filme:", palavra)
            break

    if tentativas == 0:
        print("\n💀 Fim de jogo! Você perdeu.")
        print("O filme era:", palavra)

jogo()
