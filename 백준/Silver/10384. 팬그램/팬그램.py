def main():
    D = {}
    for n in range(65, 91):
        D[chr(n)] = 0

    txt = input()
    for t in txt:
        if not ('a'<=t<='z' or 'A'<=t<='Z'):continue
        D[t.upper()] += 1
    grade = min(D.values())
    return ['Not a pangram', 'Pangram!', 'Double pangram!!', 'Triple pangram!!!'][grade]

T = int(input())
for t in range(T):
    print(f'Case {t+1}: {main()}')