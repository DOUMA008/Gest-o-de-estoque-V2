import sqlite3

conn = sqlite3.connect('produtos.db')
cursor = conn.cursor()


def cadastrar_produto():
    produto = {}
    produto['nome'] = input('Digite o nome do produto: ')
    produto['preco'] = float(input('Digite o preço do produto: '))
    produto['quantidade'] = int(input('Digite a quantidade do produto: '))
    produto['categoria'] = input('Digite a categoria do produto: ')
    return produto


def salvar_produto(produto):
    cursor.execute('''INSERT INTO produtos (nome, preco, quantidade, categoria) VALUES (?, ?, ?, ?)''',
                   (produto['nome'], produto['preco'], produto['quantidade'], produto['categoria']))
    conn.commit()


produto = cadastrar_produto()
salvar_produto(produto)
print('Produto cadastrado com sucesso!')    