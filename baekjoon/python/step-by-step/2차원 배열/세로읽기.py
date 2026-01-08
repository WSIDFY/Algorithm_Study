'''
- 5개의 단어를 모두 기억할 수 있는 2차운 리스트 형태를 만들어야 한다.
- 단어의 길이가 서로 다를 때 가장 긴 단어를 기준으로 반복하여 문자열을 만든다.(or 최대길이인 15 활용)
- 글자를 읽으려 할 때, 현재 글자의 열번호가 그 단어의 길이보다 작은지 검사해야함!
- x = list(input())으로 해야 하나씩 한 원소에 들어감, split(' ')해버리면 문자열 전체를 하나로 받음
'''
count = 5           # 입력 반복 횟수
input_arr=[]        # 입력받은 문자열들을 원소로 가지는 2차원 리스트

# 문자열 값 입력받기
for i in range(count):      # 5번 반복
    x = list(input())       # input_arr -> 입력 받은 문자열들의 2차원 리스트
    input_arr.append(x)     # ABC라고 입력하면 x는 ['A', 'B', 'C']형태로 들어감

max_length = 0      # 제일 긴 문자열의 길이값 저장할 변수

# 가장 긴 원소의 길이를 계산
for f in range(count):
    if max_length < len(input_arr[f]):
        max_length = len(input_arr[f])

# 각 문자열의 동일한 자릿수 문자를 세로로 읽어 바로바로 출력
for j in range(max_length):         # 입력받은 문자들 중 가장 긴 자릿수 만큼 반복(열)
    for k in range(count):          # 단어의 개수만큼 반복(행)

        if len(input_arr[k]) > j:   # 지금 보고있는 열의 번호보다 문자열의 길이가 크면
            print(input_arr[k][j],end='')       # 출력이 단순 문자열 출력이라 바로바로 출력하기
        else:                       # 보고있는 열의 번호가 문자열의 길이보다 크다면 패스
            continue
