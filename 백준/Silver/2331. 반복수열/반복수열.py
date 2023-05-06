def calc(n):
    ret = 0
    for t in str(n):
        ret += int(t)**P
    return ret

A, P = map(int, input().split())
S = {A}
D = {A: 1}
num = A
for _ in range(10000):
    num = calc(num)
    D[num] = D.get(num, 0)+1

ret = 0
for v in D.values():
    if v <= 3: ret += 1
print(ret)