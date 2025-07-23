nomee = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
if nomee and idade is not False:
    print(f'Seu nome é {nomee}')
    print(f'Seu nome invertido é {nomee[::-1]}')
    if ' ' in nomee:
        print('O seu nome tem espaços')
    else:
        print('O seu nome não tem espaços')
    print(f'O seu nome tem {len(nomee)} letras')
    print(f'A primeira letra do seu nome é {nomee[0]}')
    print(f'A ultima letra do seu nome é {nomee[-1]}')

else:
    print("Desculpe, você deixou os campos em branco!")