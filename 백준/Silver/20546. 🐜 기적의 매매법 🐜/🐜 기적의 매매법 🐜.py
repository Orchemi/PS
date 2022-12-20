def main():
    def calc_A(N):
        ret = 0
        for d in days:
            bought, rest = buy(N, d)
            if not bought: continue
            ret += bought
            N = rest
        return N + ret*days[-1]

    def calc_B(N):
        UD = [0]
        for i in range(1, 14):
            delta = days[i]-days[i-1]
            if delta > 0: ud = 1
            elif delta < 0: ud = -1
            else: ud = 0
            UD.append(ud)

        ret = 0
        for i in range(3, 14):
            if not (UD[i]==UD[i-1]==UD[i-2]): continue
            if not UD[i]: continue

            if UD[i] == -1:
                bought, rest = buy(N, days[i])
                if not bought: continue
                ret += bought
                N = rest

            else:
                benefit = sell(days[i], ret)
                N += benefit
                ret = 0

        return N + days[-1]*ret

    def buy(total, money):
        return total//money, total%money

    def sell(price, count):
        return price*count

    T = int(input())
    days = list(map(int, input().split()))
    A = calc_A(T)
    B = calc_B(T)

    if A > B: return 'BNP'
    if A < B: return 'TIMING'
    return 'SAMESAME'

print(main())