N = 5
arr = list(map(int, input().split()))
s_arr = sorted(arr)
while arr!=s_arr:
    for j in range(N-1):
        if arr[j] <= arr[j+1]: continue
        arr[j], arr[j+1] = arr[j+1], arr[j]
        print(*arr)