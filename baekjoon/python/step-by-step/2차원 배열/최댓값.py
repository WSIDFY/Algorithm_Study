num = 9         # 9*9 행렬의 수를 쉽게 다루기 위해 변수로 정의
arr = []        # 1차원으로 정의해도 한 번에 입력받는 원소가 9개씩이라 결국 2차원 배열 형식으로 들어감

# 행렬 원소값 입력받기
for i in range(num):
    x = list(map(int,input().split()))      # 정수로 입력받기
    arr.append(x)

max_value = 0           # 최댓값 저장할 변수
a = 0                   # 최댓값이 있는 행의 값 저장할 변수
b = 0                   # 최댓값이 있는 열의 값 저장할 변수

# 각각의 자리마다 max_value와 값의 대소를 비교하여 최댓값은 max_value에, 좌표는 a와 b에 저장
for j in range(num):
    for f in range(num):
        if max_value < arr[j][f]:
            max_value = arr[j][f]
            a = j
            b = f
        else:           # 현재 좌표의 값이 max_value에 저정되어있는 값보다 작은 값이면 패스
            continue

print(max_value)        # 최댓값 출력
print(a+1,b+1)          # 최댓값의 좌표 출력(행과 열 모두 0부터 시작하도록 구현되어있어서 +1)
