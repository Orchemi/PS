def main():
    S1 = set(input().split())
    S2 = set(input().split())
    A = sorted(list(S1|S2))
    for a in A:
        for b in A:
            print(a, b)

main()