'''
- dict사용해서 알파벳별로 값을 0으로 할당한 뒤에
- 입력받은 문자의 각 자리별로 dict에서 키값 매칭시키고 값 증가
- 마지막에 dict에서 값이 제일 큰 키값을 출력(두 개 이상이면 구분 및 '?'출력)
'''

alphabets = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
word = input().upper()

for i in range(len(word)):
    
    key = word[i]
    alphabets[key] += 1

Prosecutor_list = []
Prosecutor_list.append(max(alphabets, key=alphabets.get)) # 최대의 value를 가진 key값 모두 리스트에 추가
# 최대 value값(정수)를 구하고 저장
max_value = alphabets[Prosecutor_list[0]]
# 최대 value와 동일한 key값을 탐색
for j in range(len(alphabets)):
# 그 key값의 개수가 2개 이상이면 '?'출력

if len(len(Prosecutor_list)) > 1:
    print('?')
else:
    print(Prosecutor_list[0])

# key=alphabets.get 란? ->  
# 두 개 이상일 때를 어떻게 구분하지?

# 현재 풀이 중입니다...
