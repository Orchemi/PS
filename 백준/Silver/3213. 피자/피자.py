N = int(input())
D = {'1/2': 0, '1/4': 0, '3/4': 0}
for _ in range(N):
    k = input()
    D[k] += 1

ret = 0
ret += D['3/4']
D['1/4'] = max(D['1/4'] - D['3/4'], 0)

ret += D['1/2'] // 2
if D['1/2'] % 2:
    ret += 1
    D['1/4'] = max(D['1/4'] - 2, 0)


ret += D['1/4']//4 + 1 if D['1/4']%4 else D['1/4']//4
print(ret)