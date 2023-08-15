def main():
    N, M = map(int, input().split())
    orders = []
    for _ in range(N):
        asks = input().split()
        l = len(asks)
        if l == 1:
            orders.sort()
        elif l == 2:
            for i in range(len(orders)):
                if orders[i][1] == int(asks[1]):
                    orders.pop(i)
                    break
        else:
            n, t = int(asks[1]), int(asks[2])
            orders.append((t, n))

        if not orders:
            print('sleep')
        else:
            for t, n in orders:
                print(n, end=' ')
            print()

main()