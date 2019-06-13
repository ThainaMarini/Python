import random
n1 = int(input('Tente adivinhar o número entre 0 a 5: '))
n2 = random.randint(0,5)
print('Acertou!') if n1==n2 else print('Errou! O numero era {}'.format(n2))