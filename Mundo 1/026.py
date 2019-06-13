n1 = str(input('Digite uma frase: ')).upper().strip()
print('Na frase {} , aparece a letra A , {} vezes'.format(n1,n1.count('A')))
print('Na frase {} , aparece a letra A, pela 1° vez na posição: {}'.format(n1,n1.find('A')))
print('Na frase {} , aparece a letra A, pela ultima vez na posição: {}'.format(n1,n1.rfind('A')))
