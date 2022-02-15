N = int(input())
lst = []
for _ in range(N):
    lst.append(input())

lst.sort()
lst.sort(key=lambda x:len(x))

i = 0
while i < len(lst) -1:
    if lst[i] == lst[i+1]:
        lst.pop(i+1)
        continue
    i += 1

for i in lst:
    print(i)