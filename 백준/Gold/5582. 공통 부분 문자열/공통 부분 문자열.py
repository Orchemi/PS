def LCS(i, j):
    global memo, maxl
    if not i*j: return
    elif A[i]==B[j]:
        memo[i][j] = memo[i-1][j-1]+1
        maxl = max(maxl, memo[i][j])


A = '.'+input()
B = '.'+input()
I, J = len(A), len(B)
maxl = 0

memo = [[0]*J for _ in range(I)]
for i in range(I):
    for j in range(J):
        LCS(i, j)

print(maxl)