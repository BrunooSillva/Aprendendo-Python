primeiro_valor = input("Digite o primeiro valor: ")
segundo_valor = input("Digite o segundo valor: ")
valor1 = int(primeiro_valor)
valor2 = int(segundo_valor)

if valor1 > valor2:
    print(f'O primeiro valor {valor1} é maior que o valor dois {valor2}')
elif valor2 > valor1:
    print(f'O segundo valor {valor2} é maior que o valor um {valor1}')
else:
    print(f'Os valores são iguais')
