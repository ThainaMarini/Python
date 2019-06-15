n1 = int(input('Digite sua idade: '))
if n1<=9:
    print('Mirim')
elif (n1>9) and (n1<=14):
    print('Infantil')
elif (n1>14) and (n1<=19):
    print('Junior')
elif (n1>19) and (n1<=25):
    print('Sênior')
else:
    print('Master')