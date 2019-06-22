n1 = int(input('Digite um número: '))
fat = n1
resul = n1
while fat != 1:
    fat = fat - 1
    resul = resul * fat
print('O fatorial de {} é: {}'.format(n1,resul))

# 5! = 5*4*3*2*1 = 120
