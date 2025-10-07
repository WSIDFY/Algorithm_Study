arr = []

while True:
    A, B = map(int, input().split(' '))
    if A != 0 and B != 0:
        arr.append(A+B)
    else:
        break

for i in range(len(arr)):
    print(arr[i])
