def main():
    def check(x1, y1, x2, y2):
        global H
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2) <= H / 2

    global W, H, X, Y
    x, y = map(int, input().split())

    if (X<=x<=X+W) and (Y<=y<=Y+H): return 1
    if check(x, y, X, Y+H/2): return 1
    if check(x, y, X+W, Y+H/2): return 1
    return 0

W, H, X, Y, P = map(int, input().split())
ans = 0
for _ in range(P):
    ans += main()
print(ans)