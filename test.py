#!/usr/bin/env python3
# coding=utf-8

from sys import stdout
from random import randint as randi
from BalashM import greed
from BalashM import mod
from Ant import ant
from Balas import balas

n = 100
m = 30
test_range = 100
best_first = 0
best_second = 0
# with open('table_%dx%d.tsv' % (m,n), mode='w') as f:
with stdout as f:
    f.write('Жадный\t')
    f.write('Неувязки\t')
    f.write('Муравей\t')
    if n<30:
        f.write('Балаш\t')
    f.write('\n')
    for i in range(test_range):
        c = [randi(1, 10) for i in range(n)]
        a = [[]] * m
        for i in range(len(a)):
            a[i] = [randi(1, 10) for i in range(n)]
        b = [sum(_a) / 3 for _a in a]
        _, z1, _ = greed(c, a, b)
        f.write('%d\t' % z1)
        _, z2, _ = mod(c, a, b)
        f.write('%d\t' % z2)
        _, z4, _ = ant(c, a, b)
        f.write('%d\t' % z4)
        if n<30:
            _, z5, _ = balas(c, a, b)
            f.write('%d\t' % z5)
        f.write('\n')
        f.flush()
