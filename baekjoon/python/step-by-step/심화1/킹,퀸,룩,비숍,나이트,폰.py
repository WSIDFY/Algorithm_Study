chess_list = list(input().split())      # 동혁이가 발견한 흰색 피스들의 개수를 입력받는 리스트
orginal_set = [1,1,2,2,2,8]             # 흰색 피스가 원래 존재해야 하는 개수가 순차적으로 저장된 리스트
result = []                             # 발견한 흰색 피스에 대해 더하거나 뺴야하는 개수가 저장된 리스트


for i in range(len(chess_list)):        # 입력받은 값만큼 반복

    # 만약 올바른 세트 개수와 흰색 피스의 수가 맞지 않을 때
    if orginal_set[i] > int(chess_list[i]) or orginal_set[i] < int(chess_list[i]):

        # 있어야 하는 값에서 발견한 값을 빼기(1개 있어야하는데 2개 찾으면 1-2=-1 / 2개 있어야 하는데 1개 찾으면 2-1=1)
        value = orginal_set[i] - int(chess_list[i])     
        result.append(value)        # 결과값을 result[]에 저장

    else:
        result.append(0)    # 기존 존재해야하는 피스의 수와 찾은 피스의 수가 동일하면 필요한 피스 수가 0

# 출력문
for j in range(len(result)):
    print(int(result[j]), end=' ')

