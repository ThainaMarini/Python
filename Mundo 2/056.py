soma = 0
homem = 0
velho = ''
menos = 0
for i in range(1,4+1):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo(F/M): ')).upper()
    soma = soma + idade
    if sexo == 'M':
        if idade > homem:
            homem = idade
            velho = nome
    if sexo == 'F':
        if idade < 20:
            menos = menos + 1
print('A média de idade do grupo é: {}'.format(soma/7))
print('O homem mais velho é: {}'.format(velho))
print('Há {} mulheres com menos de 20 anos'.format(menos))