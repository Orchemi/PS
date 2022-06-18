arr = [1]*30
for _ in range(28):
    n = int(input())
    arr[n-1] = 0
    
for i in range(30):
    if arr[i]:
        print(i+1)