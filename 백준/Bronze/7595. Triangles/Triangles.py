def main(k, i):
    for _ in range(i):
        print('*', end='')
    print()
    if k==i: return
    main(k, i+1)

while True:
    n = int(input())
    if not n: break
    main(n, 1)