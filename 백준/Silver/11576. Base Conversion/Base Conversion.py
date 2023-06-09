def find_org():
    i = N-1
    time = 1
    ret = 0
    while i>=0:
        ret += time*num[i]
        i -= 1
        time *= A
    return ret

def find_ret():
    ret = [0, org]
    while True:
        if ret[1]//B:
            ret[0], ret[1] = ret[1]//B, ret[1]%B
            ret = [0]+ret
        else: break
    return ret[1:]


A, B = map(int, input().split())
N = int(input())
num = list(map(int, input().split()))
org = find_org()
ret = find_ret()
print(*ret)