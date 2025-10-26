# N:바구니의 개수 / M:자리 체인지 입력 받을 횟수
N, M = map(int, input().split())
arr = []

# N개의 바구니 각각에 순서에 맞는 숫자 넣기
for i in range(0, N): # 0,1,2,3,4 상자
    arr.append(i+1)

# M만큼 자리 변경수 입력받기 & 자릿수 교환
for r in range (0, M):
    i, j = map(int, input().split(' '))

    store = arr[i-1]
    arr[i-1] = arr[j-1]
    arr[j-1] = store

# 최종 배열 출력(공백 단위 출력 형식 변경)
for a in range(0, N):
    print(arr[a], end=' ')


"""
- 실제 배열의 인덱스는 0부터 시작이지만 문제 상에서는 1부터의 공간으로 정의하였기에 실제 공간 기준으로 연산을 하기 위해 '입력받는 값에서 -1을 해줘야 함'
- 인덱스 차이때문에 시간이 조금 걸린 것 같다.
"""
