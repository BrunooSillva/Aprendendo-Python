import os

palavra_secreta = 'bruno'
tentativas = 0
letras_acertadas = ''

while True:


    letra_digitada = input('Digite uma letra: ').lower()
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada: ', palavra_formada)       
    
    tentativas += 1
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Parabens vocÊ ganhou!')
        print('A palavra era: ', palavra_secreta)
        print('Numeros de tentativas: ', tentativas)
        break