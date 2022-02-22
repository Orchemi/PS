# 1. 최고점 구하기
n = int(input())
scores = list(map(int, input().split()))
max_val = max(scores)

# 2. 기존 점수 평균점수 구하기
avg = sum(scores) / len(scores)

# 3. 조정 평균 구하기
result = (100 / max_val) * avg
print(result)