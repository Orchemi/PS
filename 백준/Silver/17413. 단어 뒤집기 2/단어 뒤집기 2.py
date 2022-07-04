txt = input()
ret = ''
tmp = ''
i = 0
while i < len(txt):
    if txt[i] == '<':
        ret += tmp
        tmp = ''
        ret += '<'
        i += 1
        while txt[i] != '>':
            ret += txt[i]
            i += 1
        ret += '>'

    elif txt[i] == ' ':
        ret += tmp + ' '
        tmp = ''

    else:
        tmp = txt[i] + tmp

    i += 1

print(ret+tmp)