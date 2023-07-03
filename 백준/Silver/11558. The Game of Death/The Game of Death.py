def main():
    N = int(input())
    arr = [int(input())-1 for _ in range(N)]
    visited = [0]*(N+1)
    if not N-1 in set(arr): return 0

    selected = 0
    cnt = 1
    while True:
        a = arr[selected]
        if a == N-1: return cnt
        if visited[a]: return 0
        visited[a] = 1
        selected = a
        cnt += 1

T = int(input())
for _ in range(T):
    print(main())