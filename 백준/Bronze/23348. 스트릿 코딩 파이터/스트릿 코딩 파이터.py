A, B, C = map(int, input().split())
T = int(input())
max_v = 0
for _ in range(T):
    cur_v = 0
    for _ in range(3):
        a, b, c = map(int, input().split())
        cur_v += a*A + b*B + c*C

    if max_v < cur_v:
        max_v = cur_v

print(max_v)