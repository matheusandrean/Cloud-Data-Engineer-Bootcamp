a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
resto_a = a % 2
resto_b = a % 2

if resto_a == 0 or resto_b == 0:
    print('Foi digitado um número par!')
else:
    print('Nem um dos números é par!')