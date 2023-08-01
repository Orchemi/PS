def main():
    txts = input().split('x')
    if len(txts) == 1: return 0
    if txts[0]=='': return 1
    if txts[0] == '-': return -1
    return txts[0]
print(main())