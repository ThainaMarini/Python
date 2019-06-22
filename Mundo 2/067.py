n1 = 1
while n1 >= 1:
    n1 = int(input('Digite um número inteiro: '))
    if n1 >= 1:
        for i in range(1, 11):
            print('{} x {} = {}'.format(n1, i, n1*i))
