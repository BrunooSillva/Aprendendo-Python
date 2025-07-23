
#código para verificar se o número é par ou impar
try:
    numero = input('Digite um número inteiro: ')

    conversao_numero = int(numero)

    if conversao_numero % 2 == 0:
        print('Este numero é par')
    else:
        print('Este numero é impar')
except:
    print('Você não digitou um numero inteiro')

#código para checar o horário do dia
try:
    hora_do_dia = input('Digite que horas são: ')
    conversao_hora = float(hora_do_dia)

    if conversao_hora >= 0 and conversao_hora <= 11:
        print('Bom dia!')
    elif conversao_hora >= 12 and conversao_hora <= 17:
        print('Boa tarde!')
    elif conversao_hora >= 18 and conversao_hora <= 23:
        print('Boa noite!')
    else:
        print('não conheço essa hora')
except:
    print('Você não digitou uma hora valida')

#código para verificar o tamanho do nome
try:
    nome = input('Digite seu nome: ')
    
    caracteres_nome = len(nome)
    
    if caracteres_nome <= 4:
        print('Seu nome é curto')
    elif caracteres_nome >= 5 and caracteres_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é grande')
except:
    print('Voce não digitou seu nome')