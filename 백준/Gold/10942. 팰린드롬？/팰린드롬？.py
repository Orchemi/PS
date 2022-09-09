import sys
input = sys.stdin.readline
sys.setrecursionlimit(500000)

def expand_pal(s, e):
    global nums, N, mat
    if s < 0 or e >= N: return
    if nums[s] != nums[e]: return
    mat[s][e] = 1
    expand_pal(s-1, e+1)

N = int(input())
nums = list(input().split())
mat = [[0]*N for _ in range(N)]

for i in range(N):
    mat[i][i] = 1
    expand_pal(i-1, i+1)

for i in range(N-1):
    if nums[i] != nums[i+1]: continue
    mat[i][i+1] = 1
    expand_pal(i-1, i+2)

T = int(input())
for _ in range(T):
    s, e = map(lambda x: int(x)-1, input().split())
    print(mat[s][e])