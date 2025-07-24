#First-Class Function

def boasvindas(nome):
    print(f'Boas vindas {nome}!')

falar = boasvindas

falar('Bruno')

#Higher-Order Function

def executar_operacao(funcao, numero):
    return funcao(numero)

def quadrado(x):
    return x*x

print(executar_operacao(quadrado, 5))

#Criando uma função que retorna outra

def criar_saudacao(nome):
    def mensagem():
        return f'Ola {nome}'
    return mensagem

ola_bruno = criar_saudacao("Bruno")

print(ola_bruno())

#Multiplicadores com Closure

def criar_potencia(expoente):
    def potenciacao(base):
        return base ** expoente
    return potenciacao

ao_quadrado = criar_potencia(2)

ao_cubo = criar_potencia(3)

print(ao_quadrado(3))
print(ao_cubo(3))

#DESAFIO FINAL  

def criar_operacao(tipo_operacao):
    def operacao(num1, num2):
        if tipo_operacao[0] == 'A':
            return num1 + num2
        elif tipo_operacao[0] == 'S':
            return num1 - num2
        elif tipo_operacao[0] == 'M':
            return num1 * num2
        elif tipo_operacao[0] == 'D':
            return num1 / num2
    return operacao

while True:
    print('Adição, Subtração, Multiplicação, Divisão')
    operacao_desejada = input('Digite o tipo de operação que deseja realizar: ').upper()

    if operacao_desejada[0] not in 'ASMD':
        print('Oção inválida, tente novamnete.')
        continue

    funcao_tipo_operacao = criar_operacao(operacao_desejada)
    try: 
        numero1 = input('Digite o primeiro número: ')
        numero2 = input('Digite o segundo número: ')

        numero1_int = int(numero1)
        numero2_int = int(numero2)
    except:
        print('Você não digitou numeros! Tente novamente')
        continue

    print(funcao_tipo_operacao(numero1_int, numero2_int))

    saida = input('Deseja sair? s/n ').lower()
    if saida[0] == 's':
        break

