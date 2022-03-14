def fact(n):
    global factLst, fsize

    if n > fsize:
        factLst.append(n*fact(n-1))
        fsize += 1
    elif n == fsize:
        factLst.append(n*factLst[n-1])
        fsize += 1
    return factLst[n]

factLst = [1, 1]
fsize = 2
C, n = map(int, input().split())

a = fact(n)
b = fact(C-n)
c = fact(C)
print(c//(a*b))