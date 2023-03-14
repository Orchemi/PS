from collections import deque

def main():
    def BFS():
        Q = deque()
        dp = [0]*(T+1)
        for coin in coins:
            if coin > T: continue
            dp[coin] = 1
            Q.append(coin)

        while Q:
            acc = Q.popleft()
            for coin in coins:
                ssum = acc+coin
                if ssum > T: continue
                if dp[ssum]: continue
                dp[ssum] = dp[acc]+1
                Q.append(ssum)
        return dp[T] if dp[T] else -1

    N, T = map(int, input().split())
    coins = sorted(list(set([int(input()) for _ in range(N)])), reverse=True)
    return BFS()

print(main())