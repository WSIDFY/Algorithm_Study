num = int(input())
list_count = []

for i in range(0, num):
    A, B = map(int, input().split(' '))
    list_count.append(A + B) # 리스트에 연산한 값을 차례대로 추가(저장)
  
for i in range(0, num):
    print(int(list_count[i]))
