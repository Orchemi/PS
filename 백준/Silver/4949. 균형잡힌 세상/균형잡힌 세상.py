while True:
    txt = input()
    if txt=='.': break

    stack = []
    for t in txt:
        if t=='(' or t=='[':
            stack.append(t)

        elif t==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(t)
                break
        elif t==']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                stack.append(t)
                break

    print('no') if stack else print('yes')