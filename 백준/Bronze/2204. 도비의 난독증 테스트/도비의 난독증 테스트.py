while True:
    N = int(input())
    if not N: break
    arr = [input() for _ in range(N)]
    arr2 = []
    for i in range(N):
        arr2.append((arr[i].lower(), i))
    i = sorted(arr2)[0][1]
    print(arr[i])