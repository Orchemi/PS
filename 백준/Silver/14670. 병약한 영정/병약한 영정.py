def main():
    def find_pills():
        ret = []
        for d in diseases:
            p = P.get(d, -1)
            if p==-1: return ['YOU DIED']
            ret.append(p)
        return ret

    N = int(input())
    P = {}
    for _ in range(N):
        target, name = map(int, input().split())
        P[target] = name

    R = int(input())
    for _ in range(R):
        n, *diseases = list(map(int, input().split()))
        print(*find_pills())

main()