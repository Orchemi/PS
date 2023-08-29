def main():
    def make_candy_even():
        for i in range(N):
            if candy[i]%2: candy[i]+=1

    N = int(input())
    candy = list(map(int, input().split()))
    make_candy_even()

    cnt = 0
    while True:
        if len(set(candy)) == 1: return cnt
        half_candy = [c//2 for c in candy]
        candy = [half_candy[i]+half_candy[i+1] for i in range(N-1)]
        candy = [half_candy[N-1]+half_candy[0]] + candy
        make_candy_even()
        cnt += 1

T = int(input())
for _ in range(T):
    print(main())