import sys

T = int(sys.stdin.readline())
arr = []

for i in range(0, T):
    A, B = map(int, sys.stdin.readline().split(' '))
    arr.append(A+B)
    print('Case #' + str(i+1) + ': ' + str(A) + ' + ' + str(B) + ' = ' + str(arr[i]))
