'''
- dict사용해서 알파벳별로 값을 0으로 할당한 뒤에
- 입력받은 문자의 각 자리별로 dict에서 키값 매칭시키고 값 증가
- 마지막에 dict에서 값이 제일 큰 키값을 출력(두 개 이상이면 구분 및 '?'출력)
'''
# 사전은 인덱스로 접근 불가!
alphabets = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
word = input().upper()      # 입력받은 값을 대문자로 변환

max_value = 0

for i in range(len(word)):      # 입력받은 단어의 길이만큼 반복
    
    key = word[i]
    alphabets[key] += 1         # 등장한 key값의 value에 +1연산 수행

    # 최대 value값 > max_value에 저장
    if max_value < alphabets[key]:
        max_value = alphabets[key]

max_list = []       # 최대 value값을 가진 key값들을 저장할 리스트

# 최대 value값과 동일한 value값을 가진 key값을 max_list 리스트에 추가하는 반복문
for key, value in alphabets.items():
    if value == max_value:
        max_list.append(key)

# 만약 max_list의 길이가 2이상이라면(=최대 value값을 가진 key값이 두 개 이상이라면)
if len(max_list) > 1:
    print('?')
else:
    print(max_list[0])
