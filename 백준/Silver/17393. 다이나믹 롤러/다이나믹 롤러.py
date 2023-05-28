import sys
input = sys.stdin.readline

def find_mid(i):
    ink = inks[i]
    s, e = i+1, N-1
    if points[s]>ink: return 0
    if points[e]<=ink: return e-s+1

    ret = 0
    while s<=e:
        m = (s+e)//2
        if ink>=points[m]:
            ret = m-i
            s = m+1
        else:
            e = m-1
    return ret

N = int(input())
inks = list(map(int, input().split()))
points = list(map(int, input().split()))

for i in range(N-1):
    print(find_mid(i), end=' ')
print(0)