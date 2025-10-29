N, M = map(int,input().split(' '))
arr=[]
value=[]

for i in range(0,N):
    arr.append(i+1)

for z in range(0,M):
    i,j = map(int,input().split())      # 역정렬 할 인덱스 범위 입력받기
    
    # 입력된 구간을 역정렬하여 value리스트에 저장
    # reverse()는 반환값이 none이기 때문에 두 번으로 나누어 '복사된 값'을 '기존 리스트에 덮어쓰는 과정'이 필요
    value = arr[i-1:j]
    value.reverse()
    arr[i-1:j] = value    # 기존 arr리스트의 역정렬을 수행한 구간에 실제 역정렬된 값을 덮어쓰기

for a in range(len(arr)):
    print(arr[a], end=' ')
