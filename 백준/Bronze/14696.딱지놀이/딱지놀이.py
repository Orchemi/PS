N = int(input())
for _ in range(N):
    na, *la = map(int, input().split())
    nb, *lb = map(int, input().split())
    da = [0]*5
    db = [0]*5
    for a in la:
        da[a] += 1

    for b in lb:
        db[b] += 1

    lst = [da, db]
    lst.sort(key=lambda x: (x[4], x[3], x[2], x[1]))

    if lst[0]==lst[1]:
        print('D')
    elif lst[0]==da:
        print('B')
    else:
        print('A')