from flask import Flask, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = "chave-super-secreta-123"

@app.route("/")
def index():
    if "usuario" in session:
        return f"""
        <h1>Bem-vindo, {session['usuario']}!</h1>
        <p>Seu SessionID está no cookie desta página.</p>
        <a href='/logout'>Sair</a>
        """
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["usuario"] = request.form["usuario"]
        return redirect(url_for("index"))
    return """
    <h1>Login</h1>
    <form method='POST'>
        <input name='usuario' placeholder='Digite seu nome'>
        <button type='submit'>Entrar</button>
    </form>
    """

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
