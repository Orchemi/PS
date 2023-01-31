while True:
    try:
        a, b = map(int, input().split())
        total = a
        while True:
            x, y = a//b, a%b
            if not x: break
            total += x
            a = x+y
        print(total)

    except:
        break