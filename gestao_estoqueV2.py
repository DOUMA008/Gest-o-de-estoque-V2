while True:
    print("\nBem-vindo ao sistema de cadastro de produtos!")
    print('1- Cadastrar um novo produto')
    print('2- Sair do programa') 

    opcao = input('Digite a opção desejada: ')
    if opcao == '1':
        print("\nCadastro de Produto")
    elif opcao == '2':
        print("Saindo do programa. Até mais!")
        break
        
    produto = {}

    produto['nome'] = input('Digite o nome do produto: ')
    produto['preco'] = float(input('Digite o preço do produto: '))
    produto['quantidade'] = int(input('Digite a quantidade do produto: '))
    produto['categoria'] = input('Digite a categoria do produto: ')

    produto['preco_total'] = produto['preco'] * produto['quantidade']

    print("Produto cadastrado com sucesso!")
    print("Nome:", produto['nome'])
    print("Preço:", produto['preco'])
    print("Quantidade:", produto['quantidade'])
    print("Categoria:", produto['categoria'])
    print("Preço Total:", produto['preco_total'])