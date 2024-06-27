import sqlite3

try:
    # Conecta ao banco de dados SQLite
    cs = sqlite3.connect("Cookies")
    c = cs.cursor()
    
    # Executa uma consulta para listar os nomes das tabelas no banco de dados
    c.execute("SELECT tbl_name FROM sqlite_master WHERE type='table';")
    
    # Itera sobre os resultados e imprime o nome de cada tabela
    for row in c.fetchall():
        print(row[0])
    
except sqlite3.Error as e:
    print(f"Erro ao acessar o banco de dados: {e}")
    
finally:
    # Fecha a conexão com o banco de dados
    if cs:
        cs.close()
