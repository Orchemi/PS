n = int(input())


def ox(txt):
    a = ''
    lst = []

    for i in txt:

        if i == 'O':
            a += i
            continue

        elif i == 'X':
            if not a == '':
                lst.append(a)
                a = ''
            continue
        else:
            return print('입력값 오류')

    if not i == '':
        lst.append(a)

    # result 변수 초기화
    result = 0

    # 리스트의 각 O들에 대하여
    for i in lst:
        # O들의 길이
        b = len(i)
        score = b * (b+1) // 2
        result += score

    return print(result)


for i in range(n):
    c = input()
    ox(c)