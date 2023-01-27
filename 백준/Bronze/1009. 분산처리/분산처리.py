def main():
    a, b = map(int, input().split())
    ia = a%10
    c = a
    if not ia: return 10
    if ia in {1, 5, 6}: return ia

    a *= a
    s = 1
    while a%10 != ia:
        a *= ia
        s += 1

    b = b % s
    if not b: b = s
    return (ia ** b) % 10

T = int(input())
for _ in range(T):
    print(main())