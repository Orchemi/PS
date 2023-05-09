def main():
    def check1():
        for t in txt:
            if t in mu: return True
        return False

    def check2():
        cnt = 0
        cur = ''
        for t in txt:
            if t in mu:
               if cur=='mu':
                    cnt += 1
                    if cnt >= 3: return False
               else:
                   cur = 'mu'
                   cnt = 1
            else:
                if cur=='not_mu':
                    cnt += 1
                    if cnt >= 3: return False
                else:
                    cur = 'not_mu'
                    cnt = 1
        return True

    def check3():
        prev = txt[0]
        l = len(txt)
        for i in range(1, l):
            if txt[i]==prev and not txt[i] in {'e', 'o'}: return False
            prev = txt[i]
        return True


    mu = set('aeiou')
    if not check1(): return False
    if not check2(): return False
    if not check3(): return False
    return True

while True:
    txt = input()
    if txt=='end': break
    print(f'<{txt}> is {"" if main() else "not "}acceptable.')