def main():
    def check():
        txt = input()
        tl = len(txt)
        gap = 0
        while gap*(sl-1)+sl <= tl:
            si = 0
            while si+gap*(sl-1)+sl <= tl:
                flag = True
                for k in range(sl):
                    if std[k] != txt[si+k*(gap+1)]:
                        flag = False
                        break
                if flag:
                    return 1
                si += 1
            gap += 1
        return 0

    N = int(input())
    std = input()
    sl = len(std)
    cnt = 0
    for _ in range(N):
        cnt += check()
    return cnt

print(main())