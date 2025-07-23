nome = 'Bruno silva'
indice = 0
novo_nome = ''

while indice < len(nome):
    #print(f'{nome[contador]}')
    novo_nome += f'*{nome[indice]}'
    indice += 1
print(novo_nome)
print(len(nome))