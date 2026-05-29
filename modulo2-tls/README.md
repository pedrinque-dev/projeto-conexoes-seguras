# Módulo 2 — Criptografia e Handshake TLS

## Ferramenta Utilizada
- **Python 3** com biblioteca `trustme`
- **Wireshark 4.6.6** — interface Loopback
- **Google Chrome** para acesso ao servidor

---

## Passo a Passo

### 1. Instalação
```powershell
pip install trustme
```

### 2. Criar o Servidor HTTPS
Arquivo `servidor.py`:
```python
import http.server
import ssl
import trustme

# Gera certificado autoassinado
ca = trustme.CA()
server_cert = ca.issue_cert("localhost")

ca.cert_pem.write_to_path("ca.pem")
server_cert.private_key_pem.write_to_path("key.pem")
server_cert.cert_chain_pems[0].write_to_path("cert.pem")

# Sobe servidor HTTPS
servidor = http.server.HTTPServer(('localhost', 4443), http.server.SimpleHTTPRequestHandler)
contexto = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
contexto.load_cert_chain('cert.pem', 'key.pem')
servidor.socket = contexto.wrap_socket(servidor.socket, server_side=True)

print("Servidor HTTPS rodando em https://localhost:4443")
servidor.serve_forever()
```

### 3. Executar o Servidor
```powershell
cd C:\modulo2-tls
python servidor.py
```

### 4. Capturar no Wireshark
- Interface: **Adapter for loopback traffic capture**
- Filtro: `tls`
- Acessar `https://localhost:4443` no navegador

---

## Resultado

O Wireshark capturou o handshake **TLS 1.3** completo:

| Pacote | Descrição |
|--------|-----------|
| `Client Hello (SNI=localhost)` | Navegador anuncia versões e cipher suites |
| `Server Hello` | Servidor escolhe TLS 1.3 |
| `Change Cipher Spec` | Transição para comunicação cifrada |
| `Application Data` | Dados reais — ilegíveis/cifrados |

O navegador exibiu `NET::ERR_CERT_AUTHORITY_INVALID` pois o certificado é autoassinado. A conexão TLS funcionou normalmente — os dados trafegaram cifrados.

### Evidências
| Arquivo | Descrição |
|---------|-----------|
| `modulo2-print1-servidor-rodando.png` | Terminal com servidor ativo |
| `modulo2-print2a-aviso-nao-seguro.png` | Aviso de certificado inválido |
| `modulo2-print2b-detalhes-certificado.png` | Detalhes do certificado autoassinado |
| `modulo2-print3-handshake-tls.png` | Client Hello e Server Hello |
| `modulo2-print4-application-data.png` | Dados cifrados ilegíveis |

---

## Explicação Técnica

O HTTPS usa **criptografia híbrida** por razões de desempenho:

- **Assimétrica (RSA/ECC)**: usada apenas na troca de chaves — lenta, mas segura para estabelecer o segredo compartilhado
- **Simétrica (AES-256-GCM)**: usada para cifrar todo o tráfego de dados — rápida e eficiente

O TLS 1.3 com ECDHE garante **Perfect Forward Secrecy**: mesmo que a chave privada do servidor seja comprometida no futuro, sessões passadas não podem ser decifradas, pois cada sessão usa uma chave efêmera diferente.

Após o `Change Cipher Spec`, todo conteúdo aparece como `Application Data` opaco no Wireshark — exatamente o oposto do HTTP visto no Módulo 1.