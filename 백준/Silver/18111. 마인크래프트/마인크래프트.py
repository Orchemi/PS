import sys
input = sys.stdin.readline

def dig(i):
    global B, main, time, Cnt
    if main[i-1] and main[i]:
        Cnt -= 1

    time += 2 * main[i]
    B += main[i]
    main[i-1] += main[i]
    main[i] = 0


def fill(i):
    global B, main, time, Cnt
    if main[i+1] and main[i]:
        Cnt -= 1

    if B < main[i]:
        print('채울 수 없습니다.')
        return

    time += 1 * main[i]
    B -= main[i]
    main[i+1] += main[i]
    main[i] = 0


# 입력
H, W, B = map(int, input().split())
arr = []
for _ in range(H):
    arr.extend(map(int, input().split()))

# main 배열
L = max(arr)
main = [0]*(L+1)
for a in arr:
    main[a] += 1

# Cnt 계산
Cnt = 0
for m in main:
    if m:
        Cnt += 1
time = 0


# 최소 최댓값 구하기
for i in range(L+1):
    if main[i]:
        front = i
        break
for i in range(L, -1, -1):
    if main[i]:
        back = i
        break

while Cnt > 1:
    if (B >= main[front]) and (main[front] <= main[back]*2):
        fill(front)
        front += 1
    else:
        dig(back)
        back -= 1

print(time, back)