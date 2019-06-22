r = 's'
maior = 0
menos = 0
man = 0
while r == 's':
    id = int(input('Digite a idade da pessoa: '))
    s = str(input('Digite o sexo da pessoa(F/M): ')).lower()
    r = str(input('Continuar? S/N : ')).lower()
    if id > 18:
        maior = maior + 1
    if s == 'm':
        man = man + 1
    if s == 'f':
        if id < 20:
            menos = menos + 1
print('Foram cadastradas {} pessoa(s) com mais de 18 anos'.format(maior))
print('Foram cadastrados {} homem(s)'.format(man))
print('Foram cadastradas {} mulhere(s) com menos de 20 anos'.format(menos))