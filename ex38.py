import os
lista_compras = []

while True:
    print('Selecione uma opção: ')
    opcao = input('[i]nserir [a]pagar [l]istar [s]air: ').lower()

    if opcao[0] not in 'ials':
        print('opção inválida, tente novamente')
        continue

    if opcao == 'i':
        objeto = input('O que você deseja inserir: ')
        lista_compras.append(objeto)
    
    if opcao == 'a':
        indice = input('Digite o indice do produto que você quer apagar: ')
        try:
            indice_int = int(indice)
            if indice_int > len(lista_compras):
                print('Você não tem esse indice na sua lista!')
            else:
                lista_compras.pop(indice_int)
        except:
            print('Você não digitou um numero.')
       
    if opcao == 'l':
        print('Sua lista:')
        for indice, produto in enumerate(lista_compras):
            
            print(indice, produto)
    
    if opcao == 's':
        print('Saindo do programa!')
        break
