count = 5           # 입력 반복 횟수
vertical_arr = [0]  # 세로로 읽은 값들을 저장할 리스트 - 처음 값은 0이다.


for i in range(count):          # 5번 반복
    input_arr = list(input().split())       # input_arr > 입력 받은 문자열들의 행렬리스트

for j in range(len(input_arr[0])):        # 입력받은 첫 문자의 자릿수 만큼 반복(열)
    for k in range(count):          # 단어의 행(5개)만큼 반복
        vertical_arr.append(input_arr[k][j])        # 세로로 문자 하나씩 vertical_arr에 저장

print(vertical_arr)     # 중간 출력 확인

# 풀이 중입니다...
