def main():
    ret = [0, 1]
    N = int(input())
    while True:
        N -= 1
        if not N: return ret
        ret[0],ret[1] = ret[1], ret[0]+ret[1]

print(*main())