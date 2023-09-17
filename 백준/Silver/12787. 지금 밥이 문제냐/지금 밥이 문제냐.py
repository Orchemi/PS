def convert_to_10(txt):
    arr = list(map(int, txt.split('.')))
    ret = 0
    acc = 1
    while arr:
        n = arr.pop()
        ret += n*acc
        acc *= 256
    return ret

def convert_to_256(txt):
    N = int(txt)
    ret = []
    for _ in range(8):
        N, l = N//256, N%256
        ret.append(f'{l}')
    return '.'.join(ret[::-1])

T = int(input())
for _ in range(T):
    t, txt = input().split()
    if t == '1':
        print(convert_to_10(txt))
    else:
        print(convert_to_256(txt))