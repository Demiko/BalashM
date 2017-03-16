from functools import reduce


def balas_old(c, a, b):
    v = [(0, [], b)]
    for i in range(len(c)):
        vv = []
        for ii in range(len(v)):
            z, x, b = v[ii]
            bb = [0] * len(b)
            ok = True
            for iii in range(len(b)):
                _b = b[iii] - a[iii][i]
                if _b < 0:
                    ok = False
                    del bb
                    break
                bb[iii] = _b
            if ok:
                x = list(x)
                x.append(i)
                z = z + c[i]
                vv.append((z, x, bb))
        v.extend(vv)
    z, x, b = max(v, key=lambda x: x[0])
    X = [0] * len(c)
    for i in x:
        X[i] = 1
    return X, z, len(v)


def balas(c, a, b):
    Z = 0
    X = None
    r = [reduce(lambda cllctr, vl: cllctr + vl, c[i + 1:]) for i in range(len(c) - 1)] + [0]
    x = []
    z = 0
    b = [b]
    i = 0
    while i >= 0:
        if i > len(x):
            raise Exception('somehow i>len(x)')
        if i == len(c):  # maximum size of X. must go UP
            i -= 1
            continue
        if i == len(x):
            _b = b[-1]
            _b = [_b[j] - a[j][i] for j in range(len(_b))]
            if all(_b >= 0 for _b in _b):
                x.append(1)
                z += c[i]
                if z > Z:
                    Z = z
                    X = list(x)
                b.append(_b)
            else:
                x.append(0)
            if z + r[i] <= Z:  # can't be better
                if x.pop():
                    z -= c[i]
                    b.pop()
                i -= 1
                continue
            i += 1
            continue
        if x[i] == 1:  # returned 1st time. must go DOWN
            x[i] = 0
            b.pop()
            z -= c[i]
            if z + r[i] <= Z:  # can't be better
                x.pop()
                i -= 1
                continue
            i += 1
            continue
        if x[i] == 0:  # returned 2nd time. must go UP
            x.pop()
            i -= 1
            continue
    X.extend([0] * (len(c) - len(X)))
    return X, Z, None
