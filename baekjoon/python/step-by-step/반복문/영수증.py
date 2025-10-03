# X - 구매한 물건의 총액
# num - 구매한 물건의 종류의 수
# sum - 실제로 구매한 물건의 총액
# obj - 각 물건의 액수
# count - 각 물건의 갯수

X = int(input())
num = int(input())
sum = 0

for i in range(0, num):
    obj, count = map(int, input().split(' '))
    sum += obj*count

if X == sum:
    print('Yes')
else:
    print('No')
