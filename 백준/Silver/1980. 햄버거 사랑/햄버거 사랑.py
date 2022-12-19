def main():
    n, m, t = map(int, input().split())
    x, y = min(n, m), max(n, m)
    min_coke = 1e5
    max_burger = 0
    red_y = 0
    while t>0:
        a, b = t//x, t%x
        if min_coke > b:
            min_coke = b
            max_burger = red_y + a
            if not b: return max_burger, 0
        t -= y
        red_y += 1

    return max_burger, min_coke

print(*main())