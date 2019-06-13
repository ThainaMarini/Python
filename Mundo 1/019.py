import random
n1 = str(input('Nome do 1° aluno = '))
n2 = str(input('Nome do 2° aluno = '))
n3 = str(input('Nome do 3° aluno = '))
n4 = str(input('Nome do 4° aluno = '))
lista = [n1,n2,n3,n4]
trouxa = random.choice(lista)
print('O aluno que deve apagar o quadro é = {}'.format(trouxa))
