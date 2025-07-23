"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf_digitado = '746.824.890-70'
cpf_reescrito = '' #utilizado para reescrever o cpf sem ponto e traços
cpf_nove_digitos = '' #utilizado para receber os 9 primeiros digitos afim de verficar se os ultimos dois digitos são verdadeiros

resultado_digito_1 = 0
resultado_digito_2 = 0

contagem_regresiva_1 = 10 #para verificar primeiro digito
contagem_regresiva_2 = 11 #para verificar segundo digito

for digito_cpf in cpf_digitado:

    if digito_cpf == '.' or digito_cpf == '-': #primeiro if para verficar ponto ou traço
        continue
    
    cpf_reescrito += digito_cpf #reescrevendo o cpf sem os pontos e traços
    
    if len(cpf_reescrito) > 9: #aqui para quando a quantidade de caracteres de cpf_reescrito for maior que nove ele não precisa adicionar no cpf_nove_digitos
        continue
    
    cpf_nove_digitos = cpf_reescrito #atribuindo a esta variavel apenas os 9 primeiros digitos do cpf

for digito_cpf in cpf_nove_digitos:
    resultado_digito_1 += int(digito_cpf) * contagem_regresiva_1
    contagem_regresiva_1 -= 1
    

primeiro_digito = (resultado_digito_1 * 10) % 11

primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
print(f'O primeiro digito é {primeiro_digito}')

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)

cpf_dez_digitos = cpf_nove_digitos + str(primeiro_digito)


for digito_cpf in cpf_dez_digitos:
    resultado_digito_2 += int(digito_cpf) * contagem_regresiva_2
    contagem_regresiva_2 -= 1

segundo_digito = (resultado_digito_2 * 10) % 11

segundo_digito = segundo_digito if segundo_digito <= 9 else 0
print(f'O segundo digito é {segundo_digito}')

cpf_onze_digitos = cpf_dez_digitos + str(segundo_digito)

if cpf_reescrito == cpf_onze_digitos:
    print('O CPF digitado é valido')
else:
    print('O CPF digitado é invalido')
