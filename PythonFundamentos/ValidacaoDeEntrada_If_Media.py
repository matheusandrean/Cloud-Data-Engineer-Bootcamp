nota1 = int(input('Digite sua primeira nota: '))
nota2 = int(input('Digite sua segunda nota: '))
nota3 = int(input('Digite sua terceira nota: '))
media = (nota1 + nota2 + nota3) / 3

if nota1 <= 10 and nota2 <= 10 and nota3 <= 10:
    print('Média: {:.1f}'.format(media))
    # {:.1f} determina quantas casas decimais irão aparecer depois do .
else:
    print('Foi digitado algum valor incorreto!')