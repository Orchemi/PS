grade_D = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0,
}

sum_score = 0
sum_all_score = 0
for _ in range(20):
    name, score, grade = input().split()
    if grade == 'P': continue
    score = float(score)
    score_grade = grade_D[grade]
    sum_score += score
    sum_all_score += score*score_grade

print(sum_all_score/sum_score)