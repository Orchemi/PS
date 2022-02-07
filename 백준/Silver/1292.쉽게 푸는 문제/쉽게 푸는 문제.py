A, B = map(int, input().split())

i = 1
arr = [1]

while len(arr) < B:
    i += 1
    arr.extend([i]*i)

print(sum(arr[A-1:B]))