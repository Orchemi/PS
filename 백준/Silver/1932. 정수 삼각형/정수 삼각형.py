import sys
input = sys.stdin.readline

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]

iv = mat[0][0]
if N == 1:
    print(iv)
    quit()

for j in range(2):
    mat[1][j] += iv

if N == 2:
    print(max(mat[1]))
    quit()


k = 2
while k < N:
    mat[k][0] += mat[k-1][0]

    for j in range(1, k):
        mat[k][j] += max(mat[k-1][j], mat[k-1][j-1])

    mat[k][k] += mat[k-1][k-1]
    k += 1

print(max(mat[N-1]))