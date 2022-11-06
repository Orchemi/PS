import sys
input = sys.stdin.readline
from collections import deque

def check_in_D(c):
    global D
    if c in D: return True
    if c.upper() in D: return True
    if c.lower() in D: return True
    return False


def check_first(word):
    global D
    if check_in_D(word[0]): return 0, word

    D.add(word[0])
    return 1, f'[{word[0]}]{word[1:]}'


def check_middle(word):
    global D
    wl = len(word)
    for i in range(1, wl):
        if check_in_D(word[i]): continue
        D.add(word[i])
        return 1, f'{word[:i]}[{word[i]}]{word[i+1:]}'
    return 0, word

N = int(input())
D = set()
for _ in range(N):
    done = 0
    words = deque(list(input().split()))
    cur = deque()
    while words:
        word = words.popleft()
        check_ret, word = check_first(word)
        cur.append(word)
        if check_ret:
            done = 1
            break

    if done:
        print(*cur, end=' ')
        print(*words)
        continue

    cur2 = deque()
    while cur:
        word = cur.popleft()
        check_ret, word = check_middle(word)
        cur2.append(word)
        if check_ret: break

    print(*cur2, end=' ')
    print(*cur)