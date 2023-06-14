def main():
    D = {'q':0, 'u':1, 'a':2, 'c':3, 'k':4}
    txt = input()
    ret = 0
    pos = 0
    stage = [0]*4
    for t in txt:
        k = D[t]

        if k==0:
            if pos:
                pos -= 1
            else:
                ret += 1
            stage[0] += 1

        else:
            if not stage[k-1]: return -1
            stage[k-1] -= 1
            if k==4:
                pos += 1
            else:
                stage[k] += 1
    return -1 if sum(stage) else ret

print(main())