resp = 'S'
qtde = 0
soma = 0
menor = 100000
maior = 0
while resp == 'S':
    n1 = int(input('Digite um número inteiro: '))
    qtde = qtde + 1
    soma = soma + n1
    if n1 > maior:
        maior = n1
    if n1 < menor:
        menor = n1
    resp = str(input('Deseja continuar?(S/N): ')).upper()
print('A média dos valores digitado é: {}'.format(soma / qtde))
print('O menor valor digitado foi: {}'.format(menor))
print('O maior valor digitado foi: {}'.format(maior))