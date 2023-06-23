def sq(lst):
    ret = 1
    for n in lst:
        ret *= n
    return ret

N = int(input())
trees = list(map(int, input().split()))
i0 = 0
maxx = 0
for i1 in range(1, N):
    s1 = sq(trees[i0:i1])
    for i2 in range(i1+1, N):
        s2 = sq(trees[i1:i2])
        for i3 in range(i2+1, N):
            s3 = sq(trees[i2:i3])
            s4 = sq(trees[i3:])
            maxx = max(maxx, sum([s1, s2, s3, s4]))

print(maxx)