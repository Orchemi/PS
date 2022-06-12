import sys
input = sys.stdin.readline
from collections import deque
from copy import deepcopy

def check():
    txt = deque(input().rstrip())
    tl = len(txt)
    txt, tl = check2(txt, tl)

    if tl < 2: return 0

    txt_a = deepcopy(txt)
    txt_a.pop()
    txt1, tl1 = check2(txt_a, tl-1)
    if tl1 < 2: return 1

    txt_b = deepcopy(txt)
    txt_b.popleft()

    txt2, tl2 = check2(txt_b, tl-1)
    return 2 if tl2 > 1 else 1


def check2(txt, tl):
    while tl >= 2:
        if txt[0] == txt[-1]:
            txt.pop()
            txt.popleft()
            tl -= 2
            continue
        break
    return txt, tl

T = int(input().rstrip())
for _ in range(T):
    print(check())