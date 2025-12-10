from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "segredo123"  # Necessário para usar sessões

# Lista de filmes
FILMES = [
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

def escolher_filme():
    return random.choice(FILMES)

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

@app.route("/", methods=["GET", "POST"])
def index():
    if "palavra" not in session:
        session["palavra"] = escolher_filme()
        session["letras_certas"] = []
        session["letras_erradas"] = []
        session["tentativas"] = 6

    palavra = session["palavra"]
    letras_certas = session["letras_certas"]
    letras_erradas = session["letras_erradas"]
    tentativas = session["tentativas"]
    mensagem = ""

    if request.method == "POST":
        chute = request.form["letra"].upper()
        if chute.isalpha() and len(chute) == 1:
            if chute in letras_certas or chute in letras_erradas:
                mensagem = "Você já tentou essa letra!"
            elif chute in palavra:
                letras_certas.append(chute)
                mensagem = "✔ Boa! A letra está na palavra."
            else:
                letras_erradas.append(chute)
                session["tentativas"] -= 1
                tentativas -= 1
                mensagem = "✖ Letra errada!"
        else:
            mensagem = "Digite apenas uma letra válida!"

        # Verifica vitória
        if all(letra in letras_certas or letra == " " for letra in palavra):
            mensagem = f"🎉 PARABÉNS! Você acertou o filme: {palavra}"
            return render_template("index.html", palavra=mostrar_palavra(palavra, letras_certas),
                                   letras_erradas=letras_erradas, tentativas=tentativas, mensagem=mensagem, jogo_final=True)

        # Verifica derrota
        if tentativas == 0:
            mensagem = f"💀 Fim de jogo! O filme era: {palavra}"
            return render_template("index.html", palavra=mostrar_palavra(palavra, letras_certas),
                                   letras_erradas=letras_erradas, tentativas=tentativas, mensagem=mensagem, jogo_final=True)

        session["letras_certas"] = letras_certas
        session["letras_erradas"] = letras_erradas

    return render_template("index.html", palavra=mostrar_palavra(palavra, letras_certas),
                           letras_erradas=letras_erradas, tentativas=tentativas, mensagem=mensagem, jogo_final=False)

@app.route("/reiniciar")
def reiniciar():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
