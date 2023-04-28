def main():
    stack = []
    txt = input()
    acc = 1
    ret = 0
    open = {'(', '['}
    pair = {')': '(', ']': '['}
    for i in range(len(txt)):
        t = txt[i]
        if t in open:
            stack.append(t)
            acc = acc*2 if t=='(' else acc*3
        else:
            if not stack: return 0
            if pair[t] != stack[-1]: return 0
            if txt[i-1] in open: ret += acc
            acc = acc//2 if t==')' else acc//3
            stack.pop()

    return 0 if stack else ret

print(main())