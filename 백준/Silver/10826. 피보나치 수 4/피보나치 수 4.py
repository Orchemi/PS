def main():
    a, b = 0, 1
    n = 0
    N = int(input())
    while n < N:
        a, b = b, a+b
        n += 1
    return a

print(main())