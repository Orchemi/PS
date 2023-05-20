N = int(input())
arr = list(map(int, input().split()))

ret = 0
acc = arr[-1]
i = N-2
while i >= 0:
    ret += acc*arr[i]
    acc += arr[i]
    i -= 1

print(ret)