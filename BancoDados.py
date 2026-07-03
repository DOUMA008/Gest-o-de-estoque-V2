import sqlite3

conexao = sqlite3.connect('produtos.db')

cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
        id        INTEGER PRIMARY KEY AUTOINCREMENT,
        nome      TEXT    NOT NULL,
        categoria TEXT    NOT NULL,
        preco     REAL    NOT NULL,
        estoque   INTEGER NOT NULL DEFAULT 0 )
''')

conexao.commit()  # salva as alterações feitas no banco de dados
conexao.close()
print('Banco de dados criado com sucesso!')