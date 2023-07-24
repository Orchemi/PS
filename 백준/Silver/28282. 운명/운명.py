def main():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    lefts = [0]*(K+1)
    rights = [0]*(K+1)
    for i in range(N):
        lefts[arr[i]] += 1
    for i in range(N, N*2):
        rights[arr[i]] += 1

    ret = 0
    for i in range(K+1):
        if not lefts[i]: continue
        ret += lefts[i]*(N-rights[i])
    return ret

print(main())