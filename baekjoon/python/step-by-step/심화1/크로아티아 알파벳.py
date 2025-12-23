croatia = ['c=', 'c-','dz=', 'd-', 'lj', 'nj', 's=', 'z=']  # 크로아티아 문자 저장

input_string = str(input())       # 입력받을 문자열
store = []      # 식별된 크로아티아 문자 저장 리스트

for i in range(0,len(croatia)):
    if input_string.find(croatia[i]) >= 0:  # find는 값이 있으면 해당 값의 index값 리턴(없으면 -1리턴)
        store.append(croatia[i])
        input_string.remove(croatia[i])      # 문자열은 제거 불가라 수정 필요


print(store)
print(input_string)
        
print(len(store) + len(input_string))


# 현재 풀이 중...
