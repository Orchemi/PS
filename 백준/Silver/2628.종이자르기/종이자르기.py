W, H = map(int, input().split())
N = int(input())

lst_c, lst_r = [0], [0]
for _ in range(N):
    d, i = map(int, input().split())
    k = lst_c if d else lst_r
    k.append(i)

lst_c.append(W)
lst_c.sort()
lst_r.append(H)
lst_r.sort()

max_c = 0
i = 0
while lst_c[i] != W:
    if max_c < lst_c[i+1]-lst_c[i]:
        max_c = lst_c[i+1] - lst_c[i]
    i += 1

max_r = 0
i = 0
while lst_r[i] != H:
    if max_r < lst_r[i+1]-lst_r[i]:
        max_r = lst_r[i+1] - lst_r[i]
    i += 1

print(max_r*max_c)