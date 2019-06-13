import math
n1 = int(input('Digite um ângulo qualquer = '))
sen = math.sin(math.radians(n1))
cos = math.cos(math.radians(n1))
tang = math.tan(math.radians(n1))
print('O seno do ângulo de {}° é = {:.2f}°'.format(n1,sen))
print('O cosseno do ângulo de {}° é = {:.2f}°'.format(n1,cos))
print('O tangente do ângulo de {}° é = {:.2f}°'.format(n1,tang))


