A, B, C = map(int, input().split())
plus_a = (A+B)%C
plus_b = ((A%C)+(B%C))%C
multipl_a = (A*B)%C
multipl_b = ((A%C)*(B%C))%C
print("{0}\n{1}\n{2}\n{3}".format(plus_a,plus_b,multipl_a,multipl_b))
