# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


for pergunta in perguntas:
    print(f'Pergunta: {pergunta['Pergunta']}')
    
    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i}){opcao}')

    resposta = input('Digite a resposta: ')

    try:
        resposta_int = int(resposta)
    except:
        print('Erro na converção para número')

    validacao = True if pergunta['Opções'][resposta_int] == pergunta['Resposta'] else False

    if validacao:
        print('Acertou!')
    else:
        print('Errou')