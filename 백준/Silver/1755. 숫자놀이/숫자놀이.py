def convertToText(num):
    global charD
    arr = [charD[c] for c in list(str(num))]
    return ' '.join(arr)

A, B = map(int, input().split())
charD = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}

D = {}
for n in range(A, B+1):
    D[convertToText(n)] = n

cnt = 0
for k in sorted(D.keys()):
    print(D[k], end=' ')
    cnt += 1
    if cnt == 10:
        cnt = 0
        print()