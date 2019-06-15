r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1==r2==r3:
    print('O triângulo é equilátero!')
elif r1==r2 or r1==r3 or r2==r3:
    print('O triângulo é isósceles!')
else:
    print('O triângulo é escaleno!')
