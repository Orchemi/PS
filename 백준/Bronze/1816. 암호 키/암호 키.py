def main():
    N = int(input())
    n = 2
    while n <= 10**6:
        if not N%n: return 'NO'
        n += 1
    return 'YES'


T = int(input())
for _ in range(T):
    print(main())