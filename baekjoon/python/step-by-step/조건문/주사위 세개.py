A, B, C = map(int, input().split(' '))  #주사위 눈 입력

# 같은 숫자가 나왔을 때
if A == B == C:
    print(10000 + A * 1000)

# 두 개의 수가 같을 경우
elif A == B or B == C:
    print(1000 + B * 100) # 두 수 중에 하나만 선택하면 되기 때문에 B로 통일
elif A == C:
    print(1000 + A * 100)

# 모두 다른 수일 경우
elif A != B and B != C:

    if A > B and A > C:   # A가 최댓값일 때
        print(A * 100)
    
    if B > A and B > C:   # B가 최댓값일 때
        print(B * 100)
        
    if C > A and C > B:   # C가 최댓값일 때
        print(C*100)

# 조금 더 깔끔하게 풀이하고 싶다면 max()함수를 사용 -> 나 왜 이 생각을 못했을까
'''
else:
    largest_num = max(a, b, c)
    prize = largest_num * 100
print(prize)
'''
