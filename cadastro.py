def cadastrar_produto():
    produto = {}
    produto['nome'] = input('Digite o nome do produto: ')
    produto['preco'] = float(input('Digite o preço do produto: '))
    produto['quantidade'] = int(input('Digite a quantidade do produto: '))
    produto['categoria'] = input('Digite a categoria do produto: ')
    return produto