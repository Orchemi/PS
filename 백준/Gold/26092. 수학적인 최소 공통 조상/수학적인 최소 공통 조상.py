def check_parent(N):
    S = set([1, N])
    while N > 1:
        flag = 0
        for n in range(2, int(N**(1/2))+1):
            if N%n: continue
            N = N//n
            S.add(N)
            flag = 1
            break
        if not flag: break
    return S

A, B = map(int, input().split())
A_Set = check_parent(A)
B_Set = check_parent(B)
U_Set = A_Set & B_Set
print(max(list(U_Set)))