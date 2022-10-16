def move(C):
    global n, day
    jump = 2**day
    new_C = set()
    for c in C:
        for op in (1, -1):
            if 0 < c+op*jump <= n:
                new_C.add(c+op*jump)
    return new_C


n, a, b = map(int, input().split())
A, B = {a}, {b}

day = 0
while True:
    if not (A and B):
        day = -1
        break

    A, B = move(A), move(B)
    day += 1
    if A & B: break

print(day)