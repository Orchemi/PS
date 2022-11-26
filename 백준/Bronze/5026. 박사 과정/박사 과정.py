def main():
    txt = input()
    if txt == 'P=NP': return 'skipped'
    a, b = map(int, txt.split('+'))
    return a+b

N = int(input())
for _ in range(N):
    print(main())