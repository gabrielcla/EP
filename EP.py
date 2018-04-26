import json
import os.path

### => LER BANCO DE DADOS EXISTENTE/ CRIAR NOVO SE NÃO EXISTIR
if os.path.exists('dados.json')==False: 
    with open('dados.json', 'w') as arquivo:
        arquivo.write('{}')

with open('dados.json','r') as arquivo:
    estoque = json.loads(arquivo.read()) 
### => Menu Principal
def menu():
    print('\nControle de estoque')
    print('0 - sair')
    print('1 - adicionar item')
    print('2 - remover item')
    print('3 - alterar item')
    print('4 - imprimir estoque')
    print('5 - produtos em falta')
    print('6 - valor monetario total')
    x = input('Faça sua escolha:')
    print()
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
    elif x=='5':
        falta()
    elif x=='6':
        total()        
    else:
        print('\nOpcao invalida, tente denovo')
        menu()

def sair(): #Salva o dicionário e sai
    print("Até mais")
    original = json.dumps(estoque, sort_keys=True)
    with open('dados.json','w') as arquivo:
       arquivo.write(original)
       
def adicionar():
    nome = input('Nome do produto: ')
    if nome in estoque.keys():
        print("Produto já está cadastrado.\n")
        menu()
    else:
        quantidade = int(input('Quantidade inicial: '))
        while quantidade < 0:
            print('A quantidade inicial não pode ser negativa.')
            quantidade = int(input('Quantidade inicial: '))
        estoque[nome]={'quantidade':quantidade}
    
        prec = float(input('Preco Unitario: '))
        while prec < 0:
            print('O preço unitário não pode ser negativo.')
            prec = input('Preço: ')
        estoque[nome]['Preco']= prec
        menu()
        
def remover():    #Se existir ele apaga, se não ele diz que não existe
    nome = input("Nome do produto: ")
    if nome in estoque.keys():
        del estoque[nome]
        print('Produto excluido\n')
    else:
        print("Elemento não encontrado\n")
    menu()

def alterar():
    nome = input("Nome do produto: ")
    if nome in estoque.keys():     
        print('->Menu Alterar<-')
        print('0 - Voltar')
        print('1 - Quantidade')
        print('2 - Preço')
        x = input('Faça sua escolha:')
        print()
        if x=='0':
            menu()
        elif x=='1':              
            valor= int(input('Variação da quantidade: '))
            estoque[nome]['quantidade'] += valor
            print('Novo estoque de ' + nome + ': ' + str(estoque[nome]['quantidade']))
        elif x=='2':
            valor=float(input('Novo preço: '))
            estoque[nome]['Preco'] = valor
        else:
            print('Opção inválida')
    else:
        print('Elemento não encontrado\n')              
    menu()
   
def imprimir(): #Imprime o nome e a quantidade de cada produto
    print('Produto| Quantidade| Preço')
    for A in estoque.keys():
        print(A + '| '+ str(estoque[A]['quantidade'])+ ' unidades | '+ str(estoque[A]['Preco'])+ ' reais')
    print()
    menu()
    
def falta():
    print('\nProdutos em Falta:')
    for produto in estoque:
        if 'quantidade' not in estoque[produto]:
            print(produto)
        elif estoque[produto]['quantidade']<=0:
            print('{0}:{1}'.format(produto,(estoque[produto]['quantidade'])))
    menu()
    
def total():
    total=0
    for produto in estoque:
        if 'quantidade' in estoque[produto] and 'Preco' in estoque [produto]:
            total+=(estoque[produto]['quantidade']*estoque[produto]['Preco'])
        else:
            print('dados insuficientes:\no produto {0}, foi desconsiderado para o calculo\n'.format(produto))
    print('\nvalor monetário total: {0}'.format(total))
    menu()

menu()