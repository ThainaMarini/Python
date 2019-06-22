n1 = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão: '))
an = n1 + (10-1)* r
termo = 1
print('Os 10 primeiros termos dessa progressão: ')
while termo != 11:
    an = n1 + (termo-1) * r
    termo = termo + 1
    print(an)
