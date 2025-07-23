frase = 'bruno uno juno luno'
contador = 0
i = 0

while i != len(frase):
    if frase[i] == 'o':
        contador += 1
    i += 1
print(f'na frase: {frase} tem {contador} letras o')