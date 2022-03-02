print('Calcularemos sua média')

a = float(input('Digite a primeira nota: ' ))
while a > 10:
    a = float(input('Você digitou um valor incorreto, tente novamente: '))
b = float(input('Digite a segunda nota: '))
while b > 10:
    b = float(input('Você digitou um valor incorreto, tente novamente: '))
notaFinal = ((a * 4) + (b * 6)) / 10

print('Sua média final é: {:.1f}' .format(notaFinal))

