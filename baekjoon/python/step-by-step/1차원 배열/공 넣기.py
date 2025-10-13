N, M = map(int, input().split())

# 크기를 정하고 0으로 채우는 N만큼의 배열 선언
arr = list(0 for i in range(0,N))

for i in range(0,M):
    i, j, k = map(int, input().split())

    while i <= j:       # i부터 j인덱스 범위까지만 k 삽입
        arr[i-1] = k    # 리스트의 첫번째 자리부터 삽입하기 위한 -1
        i += 1

# 리스트의 원소들의 값을 공백 단위로 출력
for a in range(0, len(arr)):
    print(arr[a], end=' ')
