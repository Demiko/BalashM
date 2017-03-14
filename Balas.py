def balas(c, a, b):
    v = [(0, [], b)]
    for i in range(len(c)):
        vv = []
        for ii in range(len(v)):
            z, x, b = v[ii]
            bb = [0]*len(b)
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
    X = [0]*len(c)
    for i in x:
        X[i] = 1
    return X, z, len(v)
