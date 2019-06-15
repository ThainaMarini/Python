primo = 0
n1 = int(input('Digite um número inteiro: '))
for i in range(1,n1+1):
    if (n1 % i == 0):
        primo = primo+1
if primo == 2:
     print('O número {} é primo!'.format(n1))
else:
     print('O número {} não é primo!'.format(n1))