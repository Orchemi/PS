T = int(input())
arr = [int(input()) for _ in range(T)]
maxx = max(arr)
check = [0, 1, 2, 3]
for i in range(4, maxx+1):
    check.append(check[i-3] + (i+2)//2)

for n in arr:
    print(check[n])