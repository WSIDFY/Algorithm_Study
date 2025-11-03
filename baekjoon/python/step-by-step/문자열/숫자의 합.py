sum = 0
value = []

count = int(input())
value = list(map(int,input()))  #리스트로 입력받기

if count == len(value):    # 입력될 횟수와 입력된 숫자들의 개수가 일치한다면 합산 실행
    for i in range(len(value)):
        sum += value[i]

print(sum)

'''
상당히 간단한 문제였으나 입력받는 과정에서 split()을 제외해야 
각 숫자가 하나씩 리스트에 저장된다는 부분 때문에 시간이 지체되었다.
split()함수를 포함하여 입력을 받으면 인덱스 한 자리에 입력된 숫자들이 한 번에 들어감
(공백 단위 구분으로 입력받기 때문 : ['54321'])
'''
