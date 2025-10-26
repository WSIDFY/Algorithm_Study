# 현재 풀이 중입니다.
N, M = map(int, input().split())
arr = []

# N개의 바구니 각각에 순서에 맞는 숫자 넣기
for i in range(0, N):
    arr.append(i+1)

# M만큼 자리 변경수 입력받기 & 자릿수 교환
for r in range (0, M):
    i, j = map(int, input().split(' '))

    store = arr[i+1]
    arr[i+1] = arr[j+1]
    arr[j+1] = arr[store]

# 최종 배열 출력(공백 단위 출력 형식 변경)
for a in range(0, N):
    print(arr[a], end=' ')
