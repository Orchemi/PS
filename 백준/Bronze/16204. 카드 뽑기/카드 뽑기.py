N, M, K = map(int, input().split())
O, X = [M, K], [N-M, N-K]
print(min(O) + min(X))