r = 's'
total = 0
mais = 0
menor = 100000.00
idmenor = ''
while r == 's':
    n = str(input('Digite o nome do produto: '))
    p = float(input('Digite o preço do produto: '))
    r = str(input('Continuar? (S/N): ')).lower()
    total = total + p
    if p > 1000:
        mais = mais + 1
    if p < menor:
        menor = p
        idmenor = n
print('O total gasto é: R${:.2f}'.format(total))
print('{} produto(s) custam mais de R$1000'.format(mais))
print('O produto mais barato é: {}'.format(idmenor))