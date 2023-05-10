N = int(input())
I, J = 2*N-1, 2*N+(N-2)*2+1
M = N-1
mat = [[' ']*J for _ in range(I)]

for si, sj in ((0, 0), (0, J-N), (I-1,0), (I-1,J-N)):
    for k in range(N):
        mat[si][sj+k] = '*'

for si, sj in ((0, 0), (0, M), (M, 2*M), (M, 3*M)):
    for k in range(N):
        mat[si+k][sj+k] = '*'

for si, sj in ((0, J-N), (0, J-1), (M, M), (M, 2*M)):
    for k in range(N):
        mat[si+k][sj-k] = '*'

for lst in mat:
    print(''.join(lst).rstrip())