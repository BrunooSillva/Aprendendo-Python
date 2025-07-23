
def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

calculo = multiplicar(1,2,3,4,5)
print(calculo)

def imparoupar(numero):
    if numero % 2 == 0:
        print(f'Esse número {numero} é par')
    else:
        print(f'Esse número {numero} é impar')

imparoupar(calculo)