def main():
    global s, e, l
    txt = input()
    if len(txt) < l: return'NE'
    if not txt.startswith(s): return 'NE'
    if not txt.endswith(e): return 'NE'
    return 'DA'

N = int(input())
txt = input()
s, e = txt.split("*")
l = len(s)+len(e)

for _ in range(N):
    print(main())