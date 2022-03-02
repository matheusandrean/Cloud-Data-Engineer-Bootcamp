print('A nota minima para aprovação é 7!')

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
peso = ((nota1 * 4) + (nota2 * 6)) / 10

if peso >= 7:
    print('Parabéns, você foi aprovado com média: {}'.format(peso))
else:
    print('Infelizmente sua nota foi {}, boa sorte na próxima!'.format(peso))