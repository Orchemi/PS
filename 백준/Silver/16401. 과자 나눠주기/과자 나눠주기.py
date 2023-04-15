import sys
input = sys.stdin.readline

def main():
    K, N = map(int, input().split())
    arr = list(map(int, input().split()))
    s, e = 1, max(arr)
    ret = 0
    while s <= e:
        m = (s+e)//2
        ssum = 0
        for a in arr:
            ssum += a//m

        if ssum < K:
            e = m-1
        else:
            ret = max(ret, m)
            s = m+1
    return ret

print(main())