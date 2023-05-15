def main():
    def find_seeds():
        seeds = []
        for n1 in range(1, 10):
            for n2 in range(1, 10):
                if n1==n2: continue
                for n3 in range(1, 10):
                    if n1==n3 or n2==n3: continue
                    seeds.append([n1, n2, n3])
        return seeds

    def check():
        def check_two(tar):
            strikes, balls = 0, 0
            for i in range(3):
                if qs[i]==tar[i]: strikes += 1

            for i in range(3):
                if qs[i] in tar: balls += 1

            return strikes, balls-strikes

        new_seeds = []
        for tar in seeds:
            if check_two(tar)==(s, b):
                new_seeds.append(tar)
        return new_seeds

    N = int(input())
    seeds = find_seeds()

    for _ in range(N):
        q, s, b = map(int, input().split())
        qs = [int(n) for n in list(str(q))]
        seeds = check()

    return len(seeds)

print(main())