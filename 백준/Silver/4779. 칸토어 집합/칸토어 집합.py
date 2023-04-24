def main():
    def make_d():
        d = ['-']
        i = 1
        while i < 13:
            d.append(d[-1]+' '*(3**(i-1))+d[-1])
            i += 1
        return d

    d = make_d()
    while True:
        try:
            N = int(input())
            print(d[N])
        except:
            return

main()