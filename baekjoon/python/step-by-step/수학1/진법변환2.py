'''
10진법 수를 n진법으로 변환
print(int('변환할 문자열', 변환할 진법 정수)) 문법 활용하여 로직 구현
아스키코드도 활용해야함
참고 : https://blog.naver.com/uee8351773/224088896595
'''

# n: 변환하려는 10진수 값, base : 변환할 진법 수
def conversion(N, B) -> str:       # 해당 함수의 값을 문자열로 전달
    if N == 0:
        return '0'      # 아래에서 문자열을 반환하고 있기 때문에 동일한 타입으로 맞춰주기
    
    mod_list = []

    while N > 0:
        N, mod = divmod(N, B)        # 10진수 값을 변환할 진수 값으로 나눈 몫, 나머지를 각각 저장
        if mod >= 10:                # 나머지 값이 10 이상이면 문자로 변환해서 반환
            mod = chr(mod+55)        # ex.) mod=10 이면 55를 더해서 A의 아스키코드인 65로 만들고 문자로 변환 후 mod에 다시 저장!

        mod_list.append(str(mod))       # 연산 순차적으로 나온 나머지 값을 mod_list에 저장
        # 저장된 나머지 값들을 역순으로 저장 후, ''.join(...)을 통해 리스트를 문자열로 합친다.
    
    return ''.join(reversed(mod_list))      # 즉 여기서는 변환 과정에서 쌓인 나머지를 뒤집어서 '하나의 문자열로 합친 뒤' 반환

N, B = map(int, input().split())
print(conversion(N, B))
