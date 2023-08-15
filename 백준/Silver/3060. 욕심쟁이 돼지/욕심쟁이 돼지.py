def main():
    N = int(input())
    pigs = list(map(int, input().split()))
    S = sum(pigs)
    day = 1
    while True:
        if N < S: return day
        day += 1
        S *= 4

T = int(input())
for _ in range(T):
    print(main())