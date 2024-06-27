import socket

# Define o tempo limite padrão para operações de socket
socket.setdefaulttimeout(1)

# Cria um novo socket
s = socket.socket()

# Conecta ao servidor FTP no endereço IP e porta especificados
result = s.connect_ex(("192.168.0.200", 21))

# Verifica se a conexão foi bem-sucedida
if result == 0:
    # Recebe o banner do servidor
    banner = s.recv(1024)
    print(banner.decode('utf-8'))
else:
    print(f"Não foi possível conectar ao servidor. Código de erro: {result}")

# Fecha o socket
s.close()
