N = int(input())
count = 0

arr = list(map(int, input().split()))

if N == len(arr):

    v = int(input())

    for i in range(0,N):
        if arr[i] == v:
            count += 1

print(str(count))
