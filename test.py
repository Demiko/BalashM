#!/usr/bin/env python3
# coding=utf-8

import cProfile
from random import randint as randi

from BalashM import balash_mod

#  тестовая задача из статьи
c = [4, 7, 2, 1, 3, 5]
b = [14, 11]
a = [
    [2, 5, 1, 2, 3, 4],
    [4, 3, 2, 4, 2, 3]
    ]
#  генератор тестовых задач
n = 20
m = 10
c = [randi(1, 5) for i in range(n)]
a = [[]] * m
for i in range(len(a)):
    a[i] = [randi(1,5) for i in range(n)]
b = [randi(n, 3*n) for i in range(m)]
x, z, iters = balash_mod(c, a, b)
cProfile.run('balash_mod(c, a, b)', sort='tottime')
print('C =', c)
print('\nB =', b)
print('\nA =')
for i in range(len(a)):
    print(a[i])
print('\nX =', x)
print('Z =', z)
print('\n', iters, 'iterations')
pass
