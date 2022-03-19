def biSearch(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if mid**2 == target:
            return mid
        elif mid**2 > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

N = int(input())
print(biSearch(1, N, N))