import random
n1 = random.randint(1,3)
print('Suas opções:')
print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')
print('Sua jogada: ')
n2 = int(input(''))
print('JO')
print('KEN')
print('PÔ')
if (n2==1) and (n1==3):
    print('Eu escolhi tesoura')
    print('YOU WIN!')
elif (n2==1) and (n1==2):
    print('Eu escolhi papel')
    print('YOU LOSE!')
elif (n2==1) and (n1==1):
    print('Eu escolhi pedra')
    print('EMPATE!')

elif (n2==2) and (n1==1):
    print('Eu escolhi pedra')
    print('YOU WIN!')
elif (n2==2) and (n1==2):
    print('Eu escolhi papel')
    print('EMPATE!')
elif (n2==2) and (n1==3):
    print('Eu escolhi tesoura')
    print('YOU LOSE!')

elif (n2==3) and (n1==2):
    print('Eu escolhi papel')
    print('YOU WIN!')
elif (n2==3) and (n1==1):
    print('Eu escolhi pedra')
    print('YOU LOSE!')
elif n2>3:
    print('Número inválido')
else:
    print('Eu escolhi tesoura')
    print('EMPATE!')