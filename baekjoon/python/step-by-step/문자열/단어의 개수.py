'''
리스트에서 공백을 탐색해서 필터링 하는 구문이 중요했던 문제같다.
1. 원소의 타입이 문자인 것으로 필터링 : 불가
2. 원소가 True일때(값이 있을 때)만 새로운 리스트로 추가 : 불가
3. 원소의 길이가 1 이상인 것만 리스트로 추가되도록 필터링 : 정답
'''
S = list(map(str, input().split(' ')))    # 문자열을 공백 단위의 리스트로 입력받고
count = []      # 필터링된 단어들 넣을 리스트

for i in range(len(S)):    # 입력받은 리스트의 각 원소들 필터링
    if len(S[i]) >= 1:     # 원소의 길이가 1 이상인것만 count리스트로 추가(공백 필터링)
        count.append(S[i])
    else:
        continue           # 공백이면 skip

print(len(count))
