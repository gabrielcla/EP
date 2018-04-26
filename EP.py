import json

try:
    with open('dados.json','r') as arquivo:
        pass
except IOError:
    with open('dados.json','a') as arquivo:
        arquivo.write('{}')
finally:
    with open('dados.json','r') as arquivo:
        texto = arquivo.read()
        #texto é uma string
        estoque = json.loads(texto)


        

def menu():
    print('\nControle de estoque')
    print('0 - sair')
    print('1 - adicionar item')
    print('2 - remover item')
    print('3 - alterar item')
    print('4 - imprimir estoque')
    print('5 - produtos em falta')
    print('6 - valor monetario total')
    print('7 - controle de precos')
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
    elif x=='5':
        falta()
    elif x=='6':
        total()        
    elif x=='7':
        P_menu()
    else:
        print('\nOpcao invalida, tente denovo')
        menu()

def sair():
    print("Até mais")
    original = json.dumps(estoque, sort_keys=True)#original volta a ser string
    with open('dados.json','w') as arquivo:
       arquivo.write(original)
       
def adicionar():
    nome = input('Nome do produto: ')
    if nome in estoque.keys() and 'quantidade' in estoque[nome]:
        print("Produto já está cadastrado.")
    else:
        quantidade = int(input('Quantidade inicial: '))
        while quantidade < 0:
            print('A quantidade inicial não pode ser negativa.')
            quantidade = input('Quantidade inicial: ')
        if nome in estoque.keys():
            estoque[nome]['quantidade']= quantidade
        else:
            estoque[nome]={'quantidade':quantidade}
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
    if nome in estoque.keys() and 'quantidade' in estoque[nome] :
        valor= int(input('Quantidade: '))
        estoque[nome]['quantidade'] += valor
        print('Novo estoque de ' + nome + ': ' + str(estoque[nome]['quantidade']))
    else:
        print('Elemento não encontrado')
    menu()
   
def imprimir(): #Imprime o nome e a quantidade de cada produto
    for elemento in estoque.keys():
        if 'quantidade' in estoque[elemento]:
            print(elemento + ': ' + str(estoque[elemento]['quantidade']))
    menu()
    
def falta():
    print('\nProdutos em Falta:')
    for produto in estoque:
        if 'quantidade' not in estoque[produto]:
            print(produto)
        elif estoque[produto]['quantidade']==0:
            print(produto)
    menu()
#Fucoes do preco
def total():
    total=0
    for produto in estoque:
        if 'quantidade' in estoque[produto] and 'Preco' in estoque [produto]:
            total+=(estoque[produto]['quantidade']*estoque[produto]['Preco'])
        else:
            print('dados insuficientes:\no produto {0}, foi desconsiderado para o calculo\n'.format(produto))
    print('\nvalor monetário total: {0}'.format(total))
    menu()
    
def P_menu():
    print('\nControle de precos')
    print('0 - sair')
    print('1 - adicionar preco')
    print('2 - alterar preco')
    print('3 - imprimir precos')
    x = input('Faça sua escolha:')
    if x=='0':
        P_sair()
    elif x=='1':
        P_adicionar()
    elif x=='2':
        P_alterar()
    elif x=='3':
        P_imprimir()
    else:
        print('\nOpcao invalida, tente denovo')
        P_menu()
        
def P_sair():
    print("Até mais")
    menu()
       
def P_adicionar():
    P_nome = input('Nome do produto: ')
    if P_nome in estoque.keys() and 'Preco' in estoque[P_nome]:
        print("Preco já está cadastrado.")
    else:
        prec = int(input('Preco Unitario: '))
        while prec < 0:
            print('O preco unitario não pode ser negativo.')
            prec = input('Quantidade inicial: ')
        if P_nome in estoque.keys():
            estoque[P_nome]['Preco']= prec
        else:
            estoque[P_nome]={'Preco':prec}
    P_menu()
        
def P_alterar():
    #Se existir o produto mostra a quantidade e pede o valor a ser ADICIONADO  ao estoque, depois mostra o novo estoque
    P_nome = input("Nome do produto: ")
    if P_nome in estoque.keys() and 'Preco' in estoque[P_nome]:
        valor= int(input('Preco: '))
        estoque[P_nome]['Preco'] += valor
        print('Novo estoque de ' + P_nome + ': ' + str(estoque[P_nome]['Preco']))
    else:
        print('Preco não encontrado')
    P_menu()
def P_imprimir(): #Imprime o nome e a quantidade de cada produto
    for elemento in estoque.keys():
        if 'Preco' in estoque[elemento]:
            print(elemento + ': ' + str(estoque[elemento]['Preco']))
    P_menu()

    
    
menu()