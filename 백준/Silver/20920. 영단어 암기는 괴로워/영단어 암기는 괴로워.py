N, M = map(int, input().split())
ignores = set()
D = {}

for _ in range(N):
    word = input()
    if D.get(word, []):
        D[word][0] += 1
        continue

    if word in ignores: continue
    l = len(word)
    if l < M:
        ignores.add(word)
        continue

    D[word] = [1, l, word]

for lst in sorted(D.values(), key=lambda x:(-x[0], -x[1], x[2])):
    print(lst[2])