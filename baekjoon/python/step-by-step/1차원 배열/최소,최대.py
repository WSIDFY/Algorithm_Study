N = int(input())
arr = []

arr = list(map(int, input().split()))

if len(arr) == N:
    print(str(min(arr)), str(max(arr)))
