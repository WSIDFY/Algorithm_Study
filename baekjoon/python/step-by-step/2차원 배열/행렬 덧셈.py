'''
행렬의 덧셈에 대한 문제
- 파이썬은 배열을 사용하려면 numpy라이브러리를 설치해서 사용하거나 리스트로 구현해야 함
>>> 리스트로 풀어보기

1. 행렬의 크기를 입력받기(N, M)
2. input_list[], first_list[] 만들기
3. input_list[]에 사용자로부터 입력 받을 M개의 원소를 정수형으로 추가 +
    input_list[]의 M개까지의 원소를 first_list[]에 append * (N번 반복)

4. 3번이 완료되면 input_list[0]으로 초기화 후 second_list[]도 3번과 동일하게 진행

5. first_list[]와 second_list[]의 각 자리별로 더해서 sum_list[]에 append

6. sum_list의 각각의 원소를 M개씩 공백단위로 각각, N번 개행해서 출력
'''

N, M = map(int, input().split())                    # 입력받을 N과 M

# 첫 번째 리스트 값 입력받기
input_list, first_list = [0], [0]                   # 입력받을 값을 저장할 리스트, 첫 번째 배열 리스트 초기회   
for a in range(0, N):                               # N번의 입력
    input_list = list(map(int, input().split()))    # 공백 단위로 정수 입력받기
    for b in range(0,M):                            # M번 반복하여 fisrt_list[]에 순차 저장(초기값 0이 포함되어 있음)
        first_list.append(input_list[b])

# 두 번째 리스트 값 입력받기
input_list, second_list = [0], [0]
for c in range(0, N):                               # N번의 입력
    input_list = list(map(int, input().split()))    # 공백 단위로 정수 입력받기
    for d in range(0,M):                            # M번 반복하여 second_list[]에 순차 저장(초기값 0이 포함되어 있음)
        second_list.append(input_list[d])

# 합산된 원소를 가진 리스트 생성
sum_list = [0]                                      # 두 배열의 각 자리의 원소의 합이 되는 값을 원소로 가지는 리스트 초기화
for e in range(1, N*M+1):
    sum_list.append(first_list[e] + second_list[e]) # 두 배열의 각 자리별 합연산 수행 및 sum_list[]에 추가

idx = 1                                             # 원소의 자리를 옮겨가며 순차적으로 출력하기 위한 인덱스
# M개씩 슬라이싱해서 출력
for f in range(0, N):
    for g in range(1, M+1):                         # 0번째에는 0이 들어가있기 때문에 1번째부터 시작
        print(sum_list[idx],end=' ')
        idx += 1

    print()

'''
(참고사항)
- 파이썬 배열 만드는 방법
- 리스트의 공백단위 정수 출력
'''
