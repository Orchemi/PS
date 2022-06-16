ssum = 0
for _ in range(5):
    score = int(input())
    score = score if score >= 40 else 40
    ssum += score
    
print(ssum//5)