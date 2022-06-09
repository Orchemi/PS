import sys
input = sys.stdin.readline

H, W = map(int, input().split())
heights = list(map(int, input().split()))

# 최대 높이 계산
max_h = max(heights)

# 최대 넓이 계산
# 앞에서부터 최대 높이까지 누적
ssum1 = 0
si = 0
cur_h = 0
while heights[si] < max_h:
    cur_h = max(cur_h, heights[si])
    ssum1 += cur_h
    si += 1

# 뒤에서부터 최대 높이까지 누적
ei = W-1
cur_h = 0
while heights[ei] < max_h:
    cur_h = max(cur_h, heights[ei])
    ssum1 += cur_h
    ei -= 1

# 최대높이구간 누적
ssum1 += (ei-si+1)*max_h

print(ssum1 - sum(heights))