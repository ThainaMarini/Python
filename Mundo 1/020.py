import random
n1 = str(input('Nome do 1° aluno = '))
n2 = str(input('Nome do 2° aluno = '))
n3 = str(input('Nome do 3° aluno = '))
n4 = str(input('Nome do 4° aluno = '))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem de aprensetação será = {}'.format(lista))