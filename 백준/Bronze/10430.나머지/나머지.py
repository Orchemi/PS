A, B, C = map(int, input().split())
r1 = (A+B) % C
r2 = ((A % C)+(B % C)) % C
r3 = (A*B) % C
r4 = ((A % C)*(B % C)) % C

print(f'{r1}\n{r2}\n{r3}\n{r4}')