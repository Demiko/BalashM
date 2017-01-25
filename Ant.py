# coding=utf-8

from BalashM import mod_balas


def ant(c, a, b):
    def prio_ant(c: list, a: list, b: list) -> (list, float, int):
        b = b.copy()
        px = [0] * len(c)
        for _a, _b in zip(a, b):
            for i, _x in enumerate(ant_step(c, _a, _b)):
                px[i] += _x
        px = ((x, i) for i, x in enumerate(px))
        px = [i for _, i in sorted(px, reverse=True)]
        return px

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

    return mod_balas(c, a, b, prio_ant)
