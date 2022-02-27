N = int(input())

if N == 1:
    print(4)
    print('1 1 0 1')
    quit()

max_v = 1
ans = [N]

for n in range(1, N):
    lst = [N, n]

    cnt = 2
    while lst[-2] >= lst[-1]:
        lst.append(lst[-2] - lst[-1])
        cnt += 1

    if max_v < cnt:
        max_v = cnt
        ans = lst

print(max_v)
print(*ans)