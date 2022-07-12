def main():
    global txt

    tl = len(txt)
    d = 0
    while d < tl-1:
        i = 0
        S = set()
        while i+d+1 < tl:
            pair = txt[i] + txt[i+d+1]
            if pair in S: return 0
            S.add(pair)
            i += 1
        d += 1
    return 1


while True:
    txt = input()
    if txt == '*': break
    ret = '' if main() else 'NOT '
    print(f'{txt} is {ret}surprising.')