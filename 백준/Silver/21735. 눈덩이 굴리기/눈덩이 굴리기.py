def main():
    def dfs(time, i, size):
        if time == M or i == N-1: return size

        case1 = dfs(time+1, i+1, size+arr[i+1])
        if i+1 == N-1: return case1
        case2 = dfs(time+1, i+2, size//2+arr[i+2])
        return max(case1, case2)

    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    if N==1: return 1+arr[0]
    return dfs(0, -1, 1)

print(main())