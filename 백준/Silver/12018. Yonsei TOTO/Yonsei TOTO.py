def main():
    def calc_per_n():
        p, l = map(int, input().split())
        ms = sorted(list(map(int, input().split())))
        if p < l: return 1
        return ms[p-l]

    n, m = map(int, input().split())
    ret = []
    for _ in range(n):
        ret.append(calc_per_n())

    ret.sort(reverse=True)
    ssum = 0
    ans = 0
    while ret:
        ssum += ret.pop()
        if ssum > m: break
        ans += 1

    return ans

print(main())