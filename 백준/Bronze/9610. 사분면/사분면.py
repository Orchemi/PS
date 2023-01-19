def check(x, y):
    if not x*y: return 0
    if x > 0:
        return 1 if y > 0 else 4
    return 2 if y > 0 else 3

N = int(input())
D = {}
for _ in range(N):
    x, y = map(int, input().split())
    ret = check(x, y)
    D[ret] = D.get(ret, 0) + 1

print('Q1:', D.get(1, 0))
print('Q2:', D.get(2, 0))
print('Q3:', D.get(3, 0))
print('Q4:', D.get(4, 0))
print('AXIS:', D.get(0, 0))