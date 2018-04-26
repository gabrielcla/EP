import json
import os.path

### => LER BANCO DE DADOS EXISTENTE/ CRIAR NOVO SE NÃO EXISTIR
if os.path.exists('dados.json')==False: 
    with open('dados.json', 'w') as arquivo:
        arquivo.write('{}')
with open('dados.json','r') as arquivo:
    estoque = json.loads(arquivo.read())
def l_menu():
    print('\nControle de lojas')
    print('0 - sair')
    print('1 - adicionar loja')
    print('2 - remover loja')
    print('3 - alterar estoque da loja')
    x = input('Faça sua escolha:')
    print()
    if x=='0':
        l_sair()
    elif x=='1':
        l_dicionar()
    elif x=='2':
        l_remover()
    elif x=='3':
        l_alterar()
def l_sair():
    print("Até mais")
    original = json.dumps(estoque, sort_keys=True)
    with open('dados.json','w') as arquivo:
        arquivo.write(original)
        
def l_dicionar():
    loja = 'Loja-'+input('Nome da loja: ')
    if loja in estoque.keys():
        print("Loja já está cadastrado.\n")
        l_menu()
    estoque[loja]={}
    l_menu()
    
def l_remover():
    loja = 'Loja-'+input("Nome da loja: ")
    if loja in estoque.keys():
        del estoque[loja]
        print('Produto excluido\n')
    else:
        print("Elemento não encontrado\n")
    l_menu()
    
def l_alterar():
    loja = 'Loja-'+input("Nome da loja: ")
    if loja in estoque.keys():
        menu(loja)        
    else:
        print('Elemento não encontrado\n')
 
### => Menu Principal
def menu(loja):
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
        sair(loja)
    elif x=='1':
        adicionar(loja)
    elif x=='2':
        remover(loja)
    elif x=='3':
        alterar(loja)
    elif x=='4':
        imprimir(loja)
    elif x=='5':
        falta(loja)
    elif x=='6':
        total(loja)        
    else:
        print('\nOpcao invalida, tente denovo')
        menu(loja)

def sair(loja): #Salva o dicionário e sai
    print("Até mais")
    l_menu()
    
       
def adicionar(loja):
    nome = input('Nome do produto: ')
    if nome in estoque[loja]:
        print("Produto já está cadastrado.\n")
        menu(loja)
    else:
        quantidade = int(input('Quantidade inicial: '))
        while quantidade < 0:
            print('A quantidade inicial não pode ser negativa.')
            quantidade = int(input('Quantidade inicial: '))
        estoque[loja][nome]={'quantidade':quantidade}
    
        prec = float(input('Preco Unitario: '))
        while prec < 0:
            print('O preço unitário não pode ser negativo.')
            prec = input('Preço: ')
        estoque[loja][nome]['Preco']= prec
        menu(loja)
        
def remover(loja):    #Se existir ele apaga, se não ele diz que não existe
    nome = input("Nome do produto: ")
    if nome in estoque[loja].keys():
        del estoque[loja][nome]
        print('Produto excluido\n')
    else:
        print("Elemento não encontrado\n")
    menu(loja)

def alterar(loja):
    nome = input("Nome do produto: ")
    if nome in estoque[loja].keys():     
        print('->Menu Alterar<-')
        print('0 - Voltar')
        print('1 - Quantidade')
        print('2 - Preço')
        x = input('Faça sua escolha:')
        print()
        if x=='0':
            menu(loja)
        elif x=='1':              
            valor= int(input('Variação da quantidade: '))
            estoque[loja][nome]['quantidade'] += valor
            print('Novo estoque de ' + nome + ': ' + str(estoque[loja][nome]['quantidade']))
        elif x=='2':
            valor=float(input('Novo preço: '))
            estoque[loja][nome]['Preco'] = valor
        else:
            print('Opção inválida')
    else:
        print('Elemento não encontrado\n')              
    menu(loja)
   
def imprimir(loja): #Imprime o nome e a quantidade de cada produto
    print('Produto| Quantidade| Preço')
    for A in estoque[loja].keys():
        print(A + '| '+ str(estoque[loja][A]['quantidade'])+ ' unidades | '+ str(estoque[loja][A]['Preco'])+ ' reais')
    print()
    menu(loja)
    
def falta(loja):
    print('\nProdutos em Falta:')
    for produto in estoque[loja]:
        if 'quantidade' not in estoque[loja][produto]:
            print(produto)
        elif estoque[loja][produto]['quantidade']<=0:
            print('{0}:{1}'.format(produto,(estoque[loja][produto]['quantidade'])))
    menu(loja)
    
def total(loja):
    total=0
    for produto in estoque[loja]:
        if 'quantidade' in estoque[loja][produto] and 'Preco' in estoque[loja][produto]:
            total+=(estoque[loja][produto]['quantidade']*estoque[loja][produto]['Preco'])
        else:
            print('dados insuficientes:\no produto {0}, foi desconsiderado para o calculo\n'.format(produto))
    print('\nvalor monetário total: {0}'.format(total))
    menu(loja)

l_menu()