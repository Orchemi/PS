import sys
input = sys.stdin.readline

I, J = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(I)]
T = int(input())

filtered_v = []
for fi in range(I-2):
    for fj in range(J-2):
        arr = []
        for ai in range(fi, fi+3):
            for aj in range(fj, fj+3):
                arr.append(mat[ai][aj])
        filtered_v.append(sorted(arr)[4])

ret = 0
for v in filtered_v:
    if v >= T: ret += 1
print(ret)
