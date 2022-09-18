import sys
sys.setrecursionlimit(3000)

def check(I, J, k):
    if J==1: return 0, I-1, k
    if I==1: return J-1, 0, k
    if I==2 or J==2: return 0, 1, k
    return check(I-2, J-2, k+1)

J, I = map(int, input().split())
di, dj, k = check(I, J, 0)
si, sj = k+di, k+dj
print(si, sj)