divide = [] # 입력받은 수들을 42로 나눈 나머지값 저장 리스트
arr = [] # 중복을 제외한 나머지 값들을 저장하는 리스트

# 10개의 수를 입력받고 각각의 수를 42로 나눈 나머지를 divide리스트에 저장 
for i in range(0, 10):
    N = int(input())
    value = N % 42
    divide.append(value)

# 나머지 값들이 저장된 divide의 각각의 원소를 비교하여 중복된 원소를 제외하고 arr리스트에 저장
# 즉, 원소의 종류별로 하나씩만 arr리스트에 저장됨
for j in divide:
    if j not in arr:  # 여기가 핵심!
        arr.append(j)
    else:
        continue    # 이미 arr에 있는 원소의 종류이면 무시

print(len(arr))
