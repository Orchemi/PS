N = int(input())
arr = list(map(int, input().split()))

maxL = 0
up = eq = down = 1
for i in range(N-1):
    if arr[i] < arr[i+1]:
        up += 1
        maxL = max(maxL, down, eq)
        eq = down = 1

    elif arr[i] > arr[i+1]:
        down += 1
        maxL = max(maxL, up, eq)
        eq = up = 1

    else:
        up, down, eq = up+1, down+1, eq+1

maxL = max(maxL, up, down, eq)
print(maxL)