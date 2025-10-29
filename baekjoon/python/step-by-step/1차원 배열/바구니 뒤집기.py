# 현재 풀이 중입니다.(25.10.29)
N, M = map(int,input().split(' '))
arr=[]

for i in range(0,N):
    arr.append(i+1)

for i in range(0,M):
    s,e = map(int,input().split())

    print(arr[s:e])
