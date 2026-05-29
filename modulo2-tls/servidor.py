import http.server
import ssl
import trustme

# Gera certificado automaticamente
ca = trustme.CA()
server_cert = ca.issue_cert("localhost")

# Salva os arquivos
ca.cert_pem.write_to_path("ca.pem")
server_cert.private_key_pem.write_to_path("key.pem")
server_cert.cert_chain_pems[0].write_to_path("cert.pem")

# Sobe o servidor HTTPS
servidor = http.server.HTTPServer(('localhost', 4443), http.server.SimpleHTTPRequestHandler)
contexto = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
contexto.load_cert_chain('cert.pem', 'key.pem')
servidor.socket = contexto.wrap_socket(servidor.socket, server_side=True)

print("Servidor HTTPS rodando em https://localhost:4443")
servidor.serve_forever()
