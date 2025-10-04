import sys

# sys는 개행문자까지 입력받음(즉, 엔터키 입력까지 \n으로 입력 저장)
T = int(sys.stdin.readline())
arr = []

for i in range(0, T):
    A, B = map(int, sys.stdin.readline().split(' '))
    arr.append(A+B)

for i in range(0,T):
    print(arr[i])
