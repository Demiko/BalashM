# coding=utf-8


def mod(c,a,b):
    def prio_mod(c, a, b):
        m = len(b)
        n = len(c)
        p = [sum(b[i] - a[i][j] for i in range(m)) * c[j] for j in range(n)]
        p = [(p, i) for p, i in zip(p, range(n))]
        p.sort(reverse=True)
        return [i for _, i in p]
    return mod_balas(c,a,b,prio_mod)


def greed(c,a,b):
    def prio_greed(c, a, b):
        m = len(b)
        n = len(c)
        p = [c[j] for j in range(n)]
        p = [(p, i) for p, i in zip(p, range(n))]
        p.sort(reverse=True)
        return [i for _, i in p]
    return mod_balas(c,a,b,prio_greed)


def my(c, a, b):
    def prio_my(c, a, b):
        m = len(b)
        n = len(c)
        p = [c[j] / sum(a[i][j] / b[i] for i in range(m)) for j in range(n)]
        p = [(p, i) for p, i in zip(p, range(n))]
        p.sort(reverse=True)
        return [i for _, i in p]
    return mod_balas(c,a,b,prio_my)

def mod_balas(c: list, a: list, b: list, prio_compute) -> (list, float, int):
    """
    :param c: list
    :param a: list
    :param b: list
    :param prio_compute: function
    :return: (list, float, int)
    """
    m = len(b)
    n = len(c)
    if len(a) != m:
        print('number of rows in A must agree with B')
        raise ValueError
    if len(a[0]) != n:
        print('number of columns A must agree with C')
        raise ValueError
    if any(c <= 0 for c in c):
        print('C must be positive')
        raise ValueError
    if any(a <= 0 for a in a for a in a):
        print('A must be positive')
        raise ValueError
    if any(b <= 0 for b in b):
        print('B must be positive')
        raise ValueError
    px = prio_compute(c,a,b)
    x = buildvar(px, a, b)
    z = sum(c[j] for j in range(n) if x[j] == 1)
    pz = [j for j in range(n) if x[j] == 0]
    iters = 0
    for k in pz:
        iters += 1
        zn = 0
        xn = [0] * n
        xn[k] = 1
        bk = [(b[i] - a[i][k]) for i in range(m)]
        if all(b[i] - a[i][j] < 0 for j in range(n) if j != k for i in range(m)):
            continue
        xn = buildvar(px, a, bk, xn)
        zn = sum(c[j] * xn[j] for j in range(n))
        if zn > z:
            z = zn
            x = xn
    return x, z, iters


def buildvar(ind: list, a: list, b: list, x: list = None) -> list:
    """
    :type x: list
    :param ind: list
    :param a: list
    :param b: list
    :param x: list
    :return: list
    """
    if x is None:
        x = [0] * len(a[0])
    for j in ind:
        if x[j] == 1:
            continue
        b = [(b[i] - a[i][j]) for i in range(len(b))]
        if all(b >= 0 for b in b):
            x[j] = 1
    return x
