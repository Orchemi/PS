from heapq import heapify, heappop, heappush

def main():
    N = int(input())
    arr = list(map(int, input().split()))
    M, S = max(arr), sum(arr)
    if not (M<=1440 and S<=2880): return -1

    arr = [-n for n in arr]
    heapify(arr)

    time = 0
    while N > 1:
        a, b = heappop(arr), heappop(arr)
        if a==-1:
            N-=1
        else:
            heappush(arr, a+1)
        if b==-1:
            N-=1
        else:
            heappush(arr, b+1)
        time += 1

    if arr: time -= arr.pop()
    return time

print(main())