s=0
for I in range(1,500+1,+2):
    if (I % 3==0):
        s=s+I
print('A soma dos números ímpares que são multiplos de três entre 1 e 500 é: {}'.format(s))