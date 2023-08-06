def main():
    ret = [0]*(N+1)
    ranges = input().split(',')
    for ran in ranges:
        rans = list(map(int, ran.split('-')))
        if len(rans)==1:
            n = rans[0]
            if n > N: continue
            ret[n] = 1
        else:
            l, h = rans
            for n in range(l, h+1):
                if n > N: break
                ret[n] = 1
    return ret.count(1)

while True:
    N = int(input())
    if not N: break
    print(main())