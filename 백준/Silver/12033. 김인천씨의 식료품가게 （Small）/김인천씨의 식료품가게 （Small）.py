def main():
    N = int(input())
    arr = list(map(int, input().split()))
    ret = []
    used = [0]*(N*2)
    j = 1
    for i in range(N*2):
        if used[i]: continue
        ret.append(arr[i])
        used[i] = 1
        target = arr[i]*4//3
        while j < N*2:
            if arr[j] == target:
                used[j] = 1
                j += 1
                break
            j += 1
    return ret

T = int(input())
for t in range(T):
    print(f'Case #{t+1}:', *main())