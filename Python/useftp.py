import ftplib

try:
    # Conecta ao servidor FTP
    ftp = ftplib.FTP("192.168.0.200")
    
    # Faz login com credenciais anônimas
    ftp.login("anonymous", "anonymous")
    
    # Muda para o diretório especificado
    ftp.cwd("/var/www/")
    
    # Lista o conteúdo do diretório
    ftp.dir()
    
    # Fecha a conexão FTP
    ftp.quit()
    
except ftplib.all_errors as e:
    print(f"Erro ao se conectar ou operar no servidor FTP: {e}")
