from math import hypot
co = float(input('Digite o valor do cateto oposto = '))
ca = float(input('Digite o valor do cateto adjacente = '))
hip = hypot(co,ca)
print('O valor do comprimento da hipotenusa é {:.2f}'.format(hip))

# co = float(input('Digite o valor do cateto oposto = '))
# ca = float(input('Digite o valor do cateto adjacente = '))
# hip = (co**2 + ca**2) **(1/2)
# print('O valor do comprimento da hipotenusa é {:.2f}'.format(hip))