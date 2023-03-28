import sys
input = sys.stdin.readline

def find_gcd(l, r):
    def find_cds(n):
        lower_cds = []
        upper_cds = []
        for i in range(1, int(n**(1/2))+1):
            if n%i: continue
            lower_cds.append(i)
            if i**2==n: continue
            upper_cds.append(n//i)
        return lower_cds + upper_cds[::-1]

    init_cds = find_cds(a+l*d)
    while init_cds:
        k = init_cds.pop()
        end = True
        for j in range(l+1, r+1):
            if (a+(j*d))%k:
                end = False
                break
        if end: return k

def find_sum(l, r):
    cnt = r-l+1
    if cnt%2:
        m = (r+l)//2
        return (a+m*d)*cnt
    return (2*a+(r+l)*d)*(cnt//2)

a, d = map(int, input().split())
q = int(input())
for _ in range(q):
    n, l, r = map(lambda x: int(x)-1, input().split())
    ret = find_gcd(l, r) if n else find_sum(l, r)
    print(ret)