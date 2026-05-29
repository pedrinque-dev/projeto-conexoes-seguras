# Módulo 1 — Sniffing e Interceptação (Camada 2 e 3)

## Ferramenta Utilizada
- **Wireshark 4.6.6** com driver **Npcap**
- Sistema Operacional: Windows 10

---

## Passo a Passo

### 1. Instalação
- Baixar o Wireshark em [wireshark.org](https://www.wireshark.org/download.html)
- Durante a instalação, marcar a opção **"Install Npcap"**
- Executar o Wireshark como Administrador

### 2. Ativar Modo Promíscuo
- Acessar **Edit → Preferences → Capture**
- Marcar a opção **"Capturar pacotes em modo promíscuo"**

### 3. Iniciar Captura
- Selecionar a interface **Wi-Fi** na tela inicial
- Dar duplo clique para iniciar a captura

### 4. Gerar Tráfego
```powershell
ping google.com
nslookup google.com
```
- Acessar `http://neverssl.com` no navegador

### 5. Aplicar Filtros
| Filtro | Objetivo |
|--------|----------|
| `dns` | Consultas de nomes de domínio |
| `http` | Requisições HTTP em texto claro |
| `icmp` | Pacotes de ping |

---

## Resultado

Com o filtro `http` e acesso ao `neverssl.com`, a seguinte requisição foi capturada em **texto claro**:

```
GET /online HTTP/1.1
Host: wonderousbeautifulsplendidkiss.neverssl.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)...
Accept-Language: pt-BR,pt;q=0.9,en-US;q=0.8
Referer: http://neverssl.com/
```

### Evidências
| Arquivo | Descrição |
|---------|-----------|
| `modulo1-print1-modo-promiscuo.png` | Preferências com modo promíscuo ativado |
| `modulo1-print2-interface.png` | Interface Wi-Fi na tela inicial |
| `modulo1-print3-captura-ao-vivo.png` | Captura em tempo real |
| `modulo1-print4-filtro-dns.png` | Consultas DNS visíveis |
| `modulo1-print5-http-texto-claro.png` | Headers HTTP em texto claro |
| `modulo1-print6-ping-icmp.png` | Pacotes ICMP do ping |

---

## Explicação Técnica

Em operação normal, a NIC (Network Interface Controller) descarta todos os frames cujo endereço MAC de destino não corresponde ao seu próprio. O **modo promíscuo** desativa esse filtro no driver, fazendo com que todos os frames do segmento de rede sejam repassados ao sistema operacional, independentemente do destinatário.

Isso permite capturar passivamente o tráfego de outros dispositivos na mesma rede sem nenhuma interação com a vítima. Protocolos sem criptografia como HTTP expõem headers, cookies, User-Agent e URLs em texto legível — demonstrando a necessidade de TLS em toda comunicação de rede.