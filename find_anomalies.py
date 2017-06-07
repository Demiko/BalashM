from random import randint as randi
import BalashM, Balas, Ant


def generate_task(m,n,c,a):
    c = [randi(1, 10) for i in range(n)]
    a = [[]] * m
    for i in range(len(a)):
        a[i] = [randi(1, 10) for i in range(n)]
    b = [round(sum(_a) / 3,1) for _a in a]
    return (c,a,b)


for i in range(1,1000):
    (c,a,b) = generate_task(10,20,[1,10],[1,10])
    x1,z1,_ = BalashM.greed(c,a,b,False)
    x2,z2,_ = BalashM.mod(c,a,b,False)
    x3,z3,_ = Ant.ant(c,a,b,False)
    x,z,_ = Balas.balas(c,a,b)
    if z1==z2==z3:
        if z1==z:
            file = open('exact.txt','a')
        else:
            file = open('not_exact.txt','a')
        w = file.write
        w('Xgre = %s = %s\nXmod = %s = %s\nXant = %s = %s\nXbal = %s = %s\n\nC = %s\n\nB = %s\n\n' %
          (x1,z1,x2,z2,x3,z3,x,z,c,b))
        for s in a:
            w('%s\n' % s.__str__())
        w('\n\n\n')
        file.close()