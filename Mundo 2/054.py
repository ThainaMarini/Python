menor = 0
maior = 0
for i in range(1,7+1):
    n1 = int(input('Digite o ano de nascimento: '))
    if 2019-n1<18:
        menor = menor+1
    else:
        maior = maior+1
print('Há {} pessoas que ainda não atingiram a maioridade'.format(menor))
print('Há {} pessoas que já atingiram a maioridade'.format(maior))
