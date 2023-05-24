N = int(input())
cur = 0
ret = ['*']
while cur < N:
    new_ret = []
    for t in ret:
        new_ret.append(t+t)
    for t in ret:
        new_ret.append(t+' '*(2**cur))
    ret = new_ret
    cur += 1

[print(t.rstrip()) for t in ret]