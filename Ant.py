# coding=utf-8

from BalashM import buildvar


def ant(c: list, a: list, b: list) -> (list, float, int):
    b = b.copy()
    x = [0] * len(c)
    for _a, _b in zip(a, b):
        for i, _x in enumerate(ant_step(c, _a, _b)):
            x[i] += _x
    x = ((x, i) for i, x in enumerate(x))
    x = [i for _, i in sorted(x, reverse=True)]
    X = buildvar(x, a, b)
    return X, sum(_x * _c for _x, _c in zip(X, c))


def ant_step(c: list, a: list, b: int) -> list:
    prio = ((ca, i) for i, ca in enumerate(c / a for c, a in zip(c, a)))
    prio = [i for _, i in sorted(prio, reverse=True)]
    x = [0] * len(a)
    for i in prio:
        if b == 0:
            break
        if b < a[i]:
            x[i] = b / a[i]
            b = 0
        else:
            x[i] = 1
            b -= a[i]
    return x
