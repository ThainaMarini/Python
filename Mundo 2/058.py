import random
n2 = random.randint(0,5)
n1 = int(input('Tente adivinhar o número entre 0 a 5: '))
qtde = 0
while n1 != n2:
    n1 = int(input('Errou! Tente novamente: '))
    qtde = qtde + 1
print('Acertou! Foram necessarias {} tentativas!'.format(qtde+1))