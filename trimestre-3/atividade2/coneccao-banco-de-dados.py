import pymysql as MySQLdb

conexao = MySQLdb.connect(host="localhost",
                          user="root",
                          passwd="admin",
                          db="Teste")

banco = conexao.cursor()

banco.execute("select * from Tabela;")

for linha in banco.fetchall():
    print(f"id: {linha[0]}\nTexto: {linha[1]}\n\n")

banco.execute("insert into Tabela values(3, 'Mais Teste');")
banco.execute("insert into Tabela values(3, 'Mais Outro Teste');")
banco.execute("commit;")

conexao.close()