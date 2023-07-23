def main():
    N = int(input())
    txt = input()
    if N <= 25: return txt

    head, body, tail = txt[:11], txt[11:-11], txt[-11:]
    if body.rstrip('.').count('.'):
        head, tail = txt[:9], txt[-10:]
        return f'{head}......{tail}'
    else:
        return f'{head}...{tail}'

print(main())