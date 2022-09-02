def nextDeci(arr):
    return [*[i*10+4 for i in arr], *[i*10+7 for i in arr]]

ret = [[4, 7]]
S, E = map(int, input().split())
sl, el = len(str(S)), len(str(E))
for n in range(1, len(str(E))):
    ret.append(nextDeci(ret[-1]))

cnt1 = 0
for i in range(sl-1):
    cnt1 += 2 ** (i + 1)
for n in ret[sl-1]:
    if S > n: cnt1 += 1

cnt2 = 0
for i in range(el-1):
    cnt2 += 2 ** (i + 1)
for n in ret[el-1]:
    if E >= n: cnt2 += 1

print(cnt2 - cnt1)