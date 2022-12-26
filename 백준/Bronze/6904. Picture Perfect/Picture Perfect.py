def main(N):
    for a in range(int(N**(1/2)), 0, -1):
        if N%a: continue
        b = N//a
        print(f'Minimum perimeter is {2*(a+b)} with dimensions {a} x {b}')
        return

while True:
    N = int(input())
    if not N: break
    main(N)