import json

with open('dados.json','r') as arquivo:
    texto = arquivo.read()  #texto é uma string

estoque = json.loads(texto) #dic é um dicionario

def menu():
    print()
    print('Controle de estoque')
    print('0 - sair')
    print('1 - adicionar item')
    print('2 - remover item')
    print('3 - alterar item')
    print('4 - imprimir estoque')

    x = input('Faça sua escolha:')
    if x=='0':
        sair()
    elif x=='1':
        adicionar()
    elif x=='2':
        remover()
    elif x=='3':
        alterar()
    elif x=='4':
        imprimir()

def sair():
    print("Até mais")
    original = json.dumps(estoque, sort_keys=True) #original volta a ser string
    with open('dados.json','w') as arquivo:
       arquivo.write(original)

def adicionar():
    nome = input('Nome do produto: ')
    if nome in estoque.keys():
        print("Produto já está cadastrado.")
    else:
        quantidade = int(input('Quantidade inicial: '))
        while quantidade < 0:
            print('A quantidade inicial não pode ser negativa.')
            quantidade = input('Quantidade inicial: ')
        estoque[nome]= {'quantidade': quantidade}
        menu()

def remover():    #Se existir ele apaga, se não ele diz que não existe
    nome = input("Nome do produto: ")
    if nome in estoque.keys():
        del estoque[nome]
    else:
        print("Elemento não encontrado")
    menu()

def alterar():
    #Se existir o produto mostra a quantidade e pede o valor a ser ADICIONADO  ao estoque, depois mostra o novo estoque
    nome = input("Nome do produto: ")
    if nome in estoque.keys():
        valor= int(input('Quantidade: '))
        estoque[nome]['quantidade'] += valor
        print('Novo estoque de ' + nome + ': ' + str(estoque[nome]['quantidade']))
    else:
        print('Elemento não encontrado')
    menu()
   
def imprimir(): #Imprime o nome e a quantidade de cada produto
    for elemento in estoque.keys():
        print(elemento + ': ' + str(estoque[elemento]['quantidade']))
    menu()
    
menu()