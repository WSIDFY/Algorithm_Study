N, X = map(int, input().split())
arr = [] # 사용자로 부터 값을 입력받을 리스트
value = []  # 입력받은 값들 중 X이하인 수들만 포함하는 리스트

# 한 줄에 여러개 입력받고 리스트로 저장
arr = list(map(int, input().split()))

if len(arr) == N:

    for i in range(0, N):
        if arr[i] < X:
            value.append(arr[i])

    # 리스트 출력 형식을 공백 단위로 숫자만 출력하도록 변경
    for j in range(0, len(value)):
        print(value[j], end=' ')
