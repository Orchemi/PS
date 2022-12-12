import sys
input = sys.stdin.readline

def main():
    part, txt = input().split()
    pl = len(part)
    pi = 0
    for t in txt:
        if t == part[pi]:
            pi += 1
            if pi == pl:
                return 'Yes'
    return 'No'

while True:
    try:
        print(main())

    except:
        break