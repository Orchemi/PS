def main():
    txts = input().split('.')
    rets = []
    for txt in txts:
        l = len(txt)
        if l%2: return -1
        l //= 2
        if l%2:
            rets.append('AAAA'*(l//2)+'BB')
        else:
            rets.append('AAAA'*(l//2))

    return '.'.join(rets)

print(main())