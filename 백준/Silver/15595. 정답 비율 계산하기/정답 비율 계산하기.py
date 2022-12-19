import sys
input = sys.stdin.readline

def main():
    N = int(input())
    failed = 0
    correct = {'megalusion'}
    users = {}
    for _ in range(N):
        pn, user, ret, mem, time, lang, leng = input().split()
        if user in correct: continue
        if ret == '4':
            correct.add(user)
            failed += users.get(user, 0)
        else:
            users[user] = users.get(user, 0) + 1

    cl = len(correct)-1
    return cl*100 / (cl+failed) if cl else 0

print(main())