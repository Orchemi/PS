def main():
    def make_new_txt(n):
        new_txt = ''
        for c in txt:
            o = ord(c)-n
            o = o if o >= 97 else o-6
            new_txt += chr(o).lower()
        return new_txt

    txt = input()
    N = int(input())
    words = [input() for _ in range(N)]

    n = 1
    while True:
        new_txt = make_new_txt(n)
        for word in words:
            if len(new_txt.split(word)) > 1:
                return new_txt
        n += 1

print(main())