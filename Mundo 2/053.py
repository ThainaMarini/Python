n1 = str(input('Digite uma frase/palavra: ')).upper().replace(' ', '')
inverso = n1[::-1]
if inverso==n1:
    print(n1)
    print(inverso)
    print('A frase/palavra {} é um palíndromo!'.format(n1))
else:
    print(n1)
    print(inverso)
    print('A frase/palavra {} não é um palíndromo!'.format(n1))