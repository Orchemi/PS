import sys
input = sys.stdin.readline

def main():
    def calc_part():
        std = 1
        for i in range(4):
            std *= cows[i]
        sum_part = [std]
        for i in range(1, N-3):
            std = std // cows[i-1] * cows[i+3]
            sum_part.append(std)

        for i in range(max(1, N-3), N):
            std = std // cows[i-1] * cows[(i+3)%N]
            sum_part.append(std)

        return sum_part

    def reverse_part(n):
        delta = 0
        for i in range(n-3, n+1):
            i %= N
            sum_part[i] *= -1
            delta += sum_part[i]*2
            
        return delta
    

    N, Q = map(int, input().split())
    cows = list(map(int, input().split()))
    changes = list(map(lambda x:int(x)-1, input().split()))

    sum_part = calc_part()
    S = sum(sum_part)

    for i in changes:
        S += reverse_part(i)
        print(S)

main()