def main():
    N = int(input())
    Ls = [0, 3]
    n = 1
    while Ls[-1] < N:
        new_L = 2*Ls[-1]+(n+3)
        Ls.append(new_L)
        n += 1

    while n:
        if N <=3: return 'm' if N==1 else 'o'
        cur_L = Ls.pop()
        div = Ls[-1]
        left, right = div, cur_L-div+1

        if left < N < right: return 'm' if N == left+1 else 'o'
        if N >= right:
            N -= (right-1)
        n -= 1

print(main())