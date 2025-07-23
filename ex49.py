
# def duplicar(numero):
#     return 2 * numero

# def triplicar(numero):
#     return 3 * numero

# def quadruplicar(numero):
#     return 4 * numero

# print(duplicar(4))
# print(triplicar(4))
# print(quadruplicar(4))


def calculo(multiplicador):
    def numero(numero):
        return numero * multiplicador
    return numero

triplicar = calculo(3)
duplicar = calculo(2)

print(triplicar(3))
print(duplicar(2))

print(duplicar.__closure__)          # mostra que há uma variável lembrada
print(duplicar.__closure__[0].cell_contents)  # mostra o valor: 2
