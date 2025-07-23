print('Calculadora do Bruno')
print('Bem vindo(a)!')


def calculo(pergunta, numero1, numero2):

    if pergunta[0] == 'a':
        resultado = numero1 + numero2
        print(f'O resultado da adição é {resultado}')
    elif pergunta[0] == 's':
        resultado = numero1 - numero2
        print(f'O resultado da subtração é {resultado}')
    elif pergunta[0] == 'm':
        resultado = numero1 * numero2
        print(f'O resultado da multiplicação é {resultado}')
    elif pergunta[0] == 'd':
        resultado = numero1 / numero2
        print(f'O resultado da divisão é {resultado}')
    

while True:
    numero1 = input('Digite o primeiro número: ')
    numero2 = input('Digite o segundo número: ')

    try:
        numero1_int = int(numero1)
        numero2_int = int(numero2)
    except:
        print('Números inválidos')
        continue

    print('Temos as seguintes operações: \n[A]dição\n[S]ubtração\n[M]ultiplicação\n[D]ivisão')
    pergunta = input('Qual operação deseja realizar?').lower()

    if pergunta not in 'asmd':
        print('Operação inválida!')
        continue

    if len(pergunta) > 1:
        print('Digite apenas uma operação!')
        continue

    calculo(pergunta, numero1_int,numero2_int)
    
    sair = input('Deseja sair? [s]air: ').lower().startswith('s')
    if sair:
        break
    
   