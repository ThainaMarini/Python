maior = 0
menor = 1000
for i in range(1, 5+1):
    n1 = float(input('Digite o peso(Kg): '))
    if n1 < menor:
        menor = n1
    if n1 > maior:
        maior = n1
print('O maior peso é: {:.2f}'.format(maior))
print('O menor peso é: {:.2f}'.format(menor))