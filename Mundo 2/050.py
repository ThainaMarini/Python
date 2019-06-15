s = 0
for i in range(1,6+1):
    n1 = int(input('Digite um número inteiro: '))
    if (n1 % 2==0):
        s = s+n1
print('A soma dos numeros pares digitado é: {}'.format(s))