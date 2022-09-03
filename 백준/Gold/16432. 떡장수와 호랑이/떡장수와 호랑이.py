def check(i):
    global dds
    if len(dds[i]) == 1:
        d = dds[i].pop()
        dds[i].add(d)
        prev = i-1
        next = i+1
        if prev > -1 and (d in dds[prev]):
            dds[prev].remove(d)
            check(prev)
        if next < N  and (d in dds[next]):
            dds[next].remove(d)
            check(next)

N = int(input())
dds = []
for i in range(N):
    n, *arr = map(int, input().split())
    dds.append(set(arr))

for i in range(N):
    check(i)

for dd in dds:
    if not dd:
        print(-1)
        quit()

prev = dds[0].pop()
print(prev)
for i in range(1, N):
    if prev in dds[i]:
        dds[i].remove(prev)
    prev = dds[i].pop()
    print(prev)