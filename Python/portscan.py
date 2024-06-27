import socket
import sys
try:
    for i in range(1, 1024):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if s.connect_ex((sys.argv[1], i)) == 0:
            print(f"Porta {i} aberta")
        s.close()
except KeyboardInterrupt:
    print("Programa encerrado")
    sys.exit(1)