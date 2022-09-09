A = input()
B = input()
al, bl = len(A), len(B)
LCS = [[[0, ''] for _ in range(bl+1)] for _ in range(al+1)]

for i in range(1, al+1):
    for j in range(1, bl+1):
        LCS[i][j] = sorted([LCS[i][j-1], LCS[i-1][j]], key=lambda x:-x[0])[0]
        if A[i-1] == B[j-1]:
            n, txt = LCS[i-1][j-1]
            if n >= LCS[i][j][0]:
                LCS[i][j] = [n+1, txt+A[i-1]]

ret = LCS[al][bl]
if ret[0]:
    for a in ret:
        print(a)
else:
    print(0)