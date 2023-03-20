ret = ''
for n in bin(int(input())+1)[3:]:
    ret += '4' if n=='0' else '7'
print(ret)