def main():
    def calc_length(p1, p2):
        return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    a, b = (r1+r2)**2, (r1-r2)**2
    d = calc_length((x1, y1), (x2, y2))
    if d==0: return -1 if r1==r2 else 0
    if b > d or a < d: return 0
    if d == a or d == b: return 1
    return 2


T = int(input())
for _ in range(T):
    print(main())