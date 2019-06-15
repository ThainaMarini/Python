n1 = int(input('Digite um número inteiro: '))
print('Escolha a base de conversão:')
print('1-Para binário')
print('2-Para octal')
print('3-Para hexadecimal')
choice = int(input(''))
if choice==1:
    print('O número {} em binário é: {}'.format(n1,bin(n1)))
elif choice==2:
    print('O número {} em octa é: {}'.format(n1,oct(n1)))
else:
    print('O número {} em hexadecimal é: {}'.format(n1,hex(n1)))