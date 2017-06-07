#!/usr/bin/env python3
# coding=utf-8

from sys import stdout
from random import randint as randi
from BalashM import greed
from BalashM import mod
from BalashM import ant
from Balas import balas

n = 50
m = 20
test_range = 100
with open('table_%dx%d.tsv' % (m, n), mode='w') as f:
    # with stdout as f:
    with open('table_%dx%d_1-30.tsv' % (m, n), mode='w') as f1:
        f.write('Жадный\t')
        f1.write('Жадный\t')
        f.write('Жадный с подбором\t')
        f1.write('Жадный с подбором\t')
        f.write('Неувязки\t')
        f1.write('Неувязки\t')
        f.write('Неувязки с подбором\t')
        f1.write('Неувязки с подбором\t')
        f.write('Муравей\t')
        f1.write('Муравей\t')
        f.write('Муравей с подбором\t')
        f1.write('Муравей с подбором\t')
        if n <= 30:
            f.write('Балаш\t')
            f1.write('Балаш\t')
        f.write('\n')
        f1.write('\n')
        for i in range(test_range):
            c = [randi(1, 10) for i in range(n)]
            c1 = [randi(1, 30) for i in range(n)]
            a = [[]] * m
            for i in range(len(a)):
                a[i] = [randi(1, 10) for i in range(n)]
            b = [sum(_a) / 3 for _a in a]
            _, z1, _ = greed(c, a, b, do_iterations=False)
            f.write('%d\t' % z1)
            _, z1, _ = greed(c, a, b)
            f.write('%d\t' % z1)

            _, z1, _ = greed(c1, a, b, do_iterations=False)
            f1.write('%d\t' % z1)
            _, z1, _ = greed(c1, a, b)
            f1.write('%d\t' % z1)
            
            _, z2, _ = mod(c, a, b, do_iterations=False)
            f.write('%d\t' % z2)
            _, z2, _ = mod(c, a, b)
            f.write('%d\t' % z2)

            _, z2, _ = mod(c1, a, b, do_iterations=False)
            f1.write('%d\t' % z2)
            _, z2, _ = mod(c1, a, b)
            f1.write('%d\t' % z2)
            
            _, z3, _ = ant(c, a, b, do_iterations=False)
            f.write('%d\t' % z3)
            _, z3, _ = ant(c, a, b)
            f.write('%d\t' % z3)

            _, z3, _ = ant(c1, a, b, do_iterations=False)
            f1.write('%d\t' % z3)
            _, z3, _ = ant(c1, a, b)
            f1.write('%d\t' % z3)
            
            if n <= 100:
                _, z4, _ = balas(c, a, b)
                f.write('%d\t' % z4)
                _, z4, _ = balas(c1, a, b)
                f1.write('%d\t' % z4)
                
            f.write('\n')
            f1.write('\n')
            f.flush()
            f1.flush()
