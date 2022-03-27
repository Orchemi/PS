N = int(input())
nums = list(map(int, input().split()))

for num in nums:
    if num == 1:
        N -= 1
        continue
    elif num == 2:
        continue

    n = 2
    while num > n:
        if num % n == 0:
            N -= 1
            break

        n += 1

print(N)