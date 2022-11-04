def main():
    M = 1000000007
    ans = [0, 2, 7]
    N = int(input())
    if N < 3: return ans[N]

    cnt, cross = 2, 1
    a, b, c = ans
    while cnt < N:
        new_c = (2*cross+3*b+2*c)%M
        a, b, c = b, c, new_c
        cnt += 1
        cross += a
        cross %= M
    return c

print(main())