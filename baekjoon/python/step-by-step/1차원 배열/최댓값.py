arr = []           # 입력받은 값들을 저장할 배열
index=0            # N번째 수 출력을 위한 변수
maxvalue = 0       # 최댓값을 저장할 변수

for i in range(1,10):    # 사용자로부터 입력받은 값을 배열에 차례대로 저장하는 반복문
    num = int(input())
    arr.append(num)

for i in range(0,9):    # 입력받은 값들의 최댓값을 찾아 maxvalue에 저장하고 저장된 위치값을 저장하는 반복문
    if maxvalue < arr[i]:
        maxvalue = arr[i]
        index = i
    else:
        continue 

print(str(maxvalue))
print(str(index+1))  # 최댓값 탐색시 index가 0부터 시작했으므로 출력시에는 +1
