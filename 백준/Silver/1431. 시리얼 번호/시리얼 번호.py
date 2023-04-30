def main():
    D = {}
    N = int(input())
    for _ in range(N):
        txt = input()
        l = len(txt)
        ssum = 0
        for t in txt:
            if t.isdigit():
                ssum += int(t)
        if not D.get((l, ssum), []):
            D[(l, ssum)] = []

        D[(l, ssum)].append(txt)

    for lst in sorted(D.keys()):
        print(*sorted(D[lst]), sep='\n')

main()