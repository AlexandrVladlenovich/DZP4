import itertools
from random import randint

k = int(input("Введите степень k (после ввода, проверьте файл data.txt): "))

factor = []
for i in range(1, k +2):
    factor.append(randint(1, 101))

result = []
for i in range(len(factor)):
    if k == 1:
        result.append(f'{factor[i]}*x')
    elif k == 0:
        result.append(f'{factor[i]}')
    else:
        result.append(f'{factor[i]}*x^{k}')
    signs = randint(0, 1)
    if signs == 1:
        result.append('+')
    elif signs == 0:
        result.append('-')
    k -= 1

result.pop(-1)
result.append('=0')

record = open('data.txt', 'w')
record.write(''.join(result))
record.close()