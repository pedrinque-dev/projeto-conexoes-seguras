# Projeto Conexões Seguras

> Projeto semestral — Parte 1/3
> Faculdade de Tecnologia SENAI Felix Guisard
> Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas

---

## Sobre o Projeto

Documentação técnica e implementação prática dos principais mecanismos de segurança em redes corporativas, abrangendo sniffing de pacotes, criptografia TLS e gestão de sessões web.

[Acesse a documentação completa no GitHub Pages](https://pedrinque-dev.github.io/projeto-conexoes-seguras)

---

## Estrutura do Repositório

```
projeto-conexoes-seguras/
│
├── modulo1-sniffing/
│   ├── README.md
│   └── evidencias/
│
├── modulo2-tls/
│   ├── servidor.py
│   ├── README.md
│   └── evidencias/
│
├── modulo3-sessao/
│   ├── app.py
│   ├── README.md
│   └── evidencias/
│
├── evidencias/
├── relatorio.pdf
└── README.md
```

---

## Módulos

### [Módulo 1 — Sniffing e Interceptação](./modulo1-sniffing/)
Captura de pacotes com Wireshark em modo promíscuo. Demonstração de dados HTTP trafegando em texto claro na rede.

**Ferramenta:** Wireshark 4.6.6 + Npcap  
**Resultado:** Headers HTTP, DNS e ICMP capturados e analisados

---

### [Módulo 2 — Criptografia e Handshake TLS](./modulo2-tls/)
Servidor HTTPS local com certificado autoassinado. Captura e análise do handshake TLS 1.3.

**Ferramenta:** Python 3 + trustme + Wireshark  
**Resultado:** Client Hello, Server Hello, Change Cipher Spec e Application Data cifrado

---

### [Módulo 3 — Segurança na Camada de Aplicação](./modulo3-sessao/)
Aplicação Flask com autenticação por sessão. Captura de cookie SessionID em texto claro via HTTP.

**Ferramenta:** Python 3 + Flask + Wireshark  
**Resultado:** Set-Cookie exposto no tráfego HTTP sem criptografia

---

## Comparativo HTTP vs HTTPS

| Característica | HTTP | HTTPS |
|----------------|------|-------|
| Criptografia | Nenhuma | TLS 1.3 AES-256 |
| Cookie visível | Texto claro | Cifrado |
| Headers visíveis | Texto claro | Cifrado |
| Risco principal | Session Hijacking | Certificado inválido |

---

## Relatório Técnico

[Download do Relatório PDF](./relatorio.pdf)

---

## Tecnologias Utilizadas

- Wireshark 4.6.6 + Npcap
- Python 3 + Flask
- trustme (certificado TLS)

---

## Equipe

| Nome |
|------|
| Bárbara Yasmin Pimenta dos Santos Tobias |
| Luana Gabrielle Ferreira Guedes Paes |
| Pedro Augusto Lombardi da Costa |
| Ruan Monteiro Brito |