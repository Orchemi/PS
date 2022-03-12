def func(i, s, L, C):
    if i == L:
        global stack
        cnt = 0
        for ch in stack:
            if ch in 'aeiou':
                cnt += 1

        if (cnt>=1) and (L-cnt)>=2:
            print(''.join(stack))
        return

    if s == C:
        return

    for k in range(s, C):
        stack.append(chs[k])
        func(i+1, k+1, L, C)
        stack.pop()

L, C = map(int, input().split())
chs = sorted(list(input().split()))

stack = []
func(0, 0, L, C)