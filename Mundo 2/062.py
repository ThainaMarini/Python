n1 = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão: '))
termo = 1
total = 0
cont = 1
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(n1)
        n1 = n1 + r
        cont = cont + 1
    mais = int(input('Você gostaria de adicionar mais termos? Quantos? : '))
