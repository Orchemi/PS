N = int(input())
lst = []

for i in range(N):
    lst.insert(0, int(input()))

cnt = 0
max_val = lst[0]+1

for n in lst:
    while n >= max_val:
        n -= 1
        cnt += 1


    max_val = n

print(cnt)