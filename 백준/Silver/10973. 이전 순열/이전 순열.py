def main():
    N = int(input())
    arr = list(map(int, input().split()))

    i = N-1
    while True:
        if i==0: return [-1]
        if arr[i] < arr[i-1]:
            S = set(arr[i-1:N])
            t = arr[i-1]
            break
        i -= 1

    ret = arr[:i-1]
    t -= 1
    while True:
        if t in S:
            ret.append(t)
            S.remove(t)
            break
        t -= 1

    return ret + sorted(list(S), reverse=True)

print(*main())