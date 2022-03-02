a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

'''Precisamos definir que a entrada dos números são "inteiros" caso contrário será considerado 'str' 
e não efetuará o calculo.'''

soma = a + b
subtracao = a - b
divisao = a / b
multi = a * b

resultado = ("A soma dos números é: {}\n"
      "A subtração dos números é: {}\n"
      "A divisão dos números é: {}\n"
      "A multiplicação dos números é: {}" .format(soma,
                                                  subtracao,
                                                  divisao,
                                                  multi))
print(resultado)
