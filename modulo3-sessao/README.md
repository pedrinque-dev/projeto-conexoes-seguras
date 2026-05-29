# Módulo 3 — Segurança na Camada de Aplicação

## Ferramenta Utilizada
- **Python 3** com framework **Flask**
- **Wireshark 4.6.6** — interface Loopback
- **Google Chrome**

---

## Passo a Passo

### 1. Instalação
```powershell
pip install flask
```

### 2. Criar a Aplicação
Arquivo `app.py`:
```python
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
```

### 3. Executar a Aplicação
```powershell
cd C:\modulo3-sessao
python app.py
```

### 4. Capturar o Cookie no Wireshark
- Interface: **Adapter for loopback traffic capture**
- Filtro: `http`
- Fazer login em `http://localhost:5000`
- Localizar pacote `HTTP/1.1 302 FOUND` e expandir o campo `Set-Cookie`

---

## Resultado

No pacote de resposta ao POST /login, o Wireshark revelou o cookie em **texto claro**:

```
Set-Cookie: session=eyJlc3VhcmlvIjoiUGVkcm8ifQ.ahZo4g.0KEfEOy1JSjcwkVg-thueNnHzXA
HttpOnly; Path=/
```

**Análise das flags presentes e ausentes:**

| Flag | Status | Implicação |
|------|--------|------------|
| `HttpOnly` | Presente | Protege contra XSS |
| `Secure` | Ausente | Cookie enviado em HTTP — vulnerável a sniffing |
| `SameSite` | Ausente | Vulnerável a CSRF |

### Evidências
| Arquivo | Descrição |
|---------|-----------|
| `modulo3-print1-app-rodando.png` | Terminal com Flask ativo |
| `modulo3-print2-login.png` | Página de login |
| `modulo3-print3-logado.png` | Página após autenticação |
| `modulo3-print4-cookie-texto-claro.png` | Set-Cookie visível no Wireshark |

---

## Explicação Técnica

### O que é um Cookie SessionID?
Após o login, o servidor gera um identificador único (SessionID) e o envia ao navegador via `Set-Cookie`. O navegador armazena esse valor e o reenvia automaticamente em todas as requisições seguintes, permitindo que o servidor identifique o usuário sem nova autenticação.

### Riscos com HTTP puro
Com HTTP, o SessionID trafega em texto claro na rede. Qualquer pessoa com Wireshark na mesma rede pode capturá-lo e usá-lo para se passar pelo usuário — ataque chamado **Session Hijacking**.

### Como o HTTPS protege os cookies
O HTTPS cifra toda a camada de transporte com TLS, incluindo os headers onde os cookies trafegam. Com HTTPS, o Wireshark mostraria apenas `Application Data` ilegível.

### Boas práticas para desenvolvedores
```python
# Cookie seguro em Flask
app.config.update(
    SESSION_COOKIE_SECURE=True,      # Só envia em HTTPS
    SESSION_COOKIE_HTTPONLY=True,    # Bloqueia acesso via JavaScript
    SESSION_COOKIE_SAMESITE='Strict' # Previne CSRF
)
```