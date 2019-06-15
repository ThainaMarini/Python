n1 = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão: '))
an = n1 + (10-1)* r
print('Os 10 primeiros termos dessa progressão: ')
for i in range(n1,an+r,r):
    print(i)