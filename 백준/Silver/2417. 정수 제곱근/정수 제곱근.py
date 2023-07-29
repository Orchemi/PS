def main():
    N = int(input())
    s, e = 0, 2**32
    q = 0
    while s<=e:
        m = (s+e)//2
        if m**2 >= N:
            q = m
            e = m-1
        else:
            s = m+1
    return q

print(main())