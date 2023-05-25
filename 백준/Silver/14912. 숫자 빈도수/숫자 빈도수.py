n, m = input().split()
ret = 0
for k in range(1, int(n)+1):
    ret += str(k).count(m)
print(ret)