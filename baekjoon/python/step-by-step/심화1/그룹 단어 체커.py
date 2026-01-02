'''
그룹단어의 정의 : 같은 문자면 연속되서 존재해야 함
예를 들어 aabbcc는 그룹단어임 근데, aabbacc는 a하나가 따로 배치되어 있기 때문에 그룹X

우선 for문으로 입력받은 횟수만큼 반복
1. 문자열 입력받기 작업

2. 그룹단어인지 확인
> 이미 존재하는 문자가 한번 더 인식되는지에 대한 로직 필요
> 각 문자별로 인식된 문자를 새 리스트에 저장(중복X)하고 그 다음 문자를 비교할 때

1.)직전 값과 같은지 비교 + 2.)리스트에 저장된 값인지 비교
직전값과 같지않고 + 리스트에 저장된 값이 아니라면 = 해당 문자를 리스트에 저장
직전값과 같지 않고 + 리스트에 저장된 값이라면 = 그룹합수 아님*
직전값과 같고 + 리스트에 저장된 값이 아니라면 = 해당 논리는 존재 불가 
직전값과 같고 + 리스트에 저장된 값이라면 = 무시하고 진행

3. 그룹단어이면 value += 1

4. value 출력

풀이 중...
'''

count = int(input())

group_check_list = [0]
value = 0

for i in range(count):
    text = str(input())
    
    for j in range(len(text)):

        # 문자가 직전 값과 같지 않고, 리스트에 저장되어 있지 않다면
        if group_check_list[-1] != text[j] and group_check_list.find(text[j]) == -1:    
            group_check_list.append(text[i])        # 문자를 리스트에 추가

        # 문자가 직전값과 같고, 리스트에 저장되어 있는 값이라면
        elif group_check_list[-1] == text[j] and group_check_list.find(text[j]) > -1:
            continue    # 무시하고 진행

        # 문자가 직전값과 같지 않고, 리스트에 저장되어 있는 값이라면(그룹단어X)
        elif group_check_list[-1] != text[j] and group_check_list.find(text[j]) > -1:
            group_check_list = group_check_list.clear()
            break       # 해당 문자열은 건너뛰기
    
    if len(group_check_list) > 0:
        value += 1
    
print(value)
