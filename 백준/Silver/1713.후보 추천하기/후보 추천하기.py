import sys
input = sys.stdin.readline

N = int(input())
T = int(input())
votes = list(map(int, input().split()))

photo = {}
for i in range(T):
    if votes[i] in photo:
        photo[votes[i]][0] += 1

    else:
        if len(photo) < N:
            photo[votes[i]] = [1, i]
        else:
            del_lst = sorted(photo.items(), key=lambda x: (x[1][0], x[1][1]))
            del_key = del_lst[0][0]
            del(photo[del_key])
            photo[votes[i]] = [1, i]

ans_lst = sorted(photo.keys())
print(*ans_lst)