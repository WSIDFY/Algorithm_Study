'''
n진수 -> 10진수 변환
* 파이썬에서는 int(string_number, base)문법으로 쉽게 변환 가능
ex.) print(int('101', 2)) : 2진수인 101을 10진수로 변환 = 5
단, 10진수-> n진수 혹은, 진법 간 변환(n>m)은 직접 구현이 필요, 해당 방식은 정수만 적용 가능
참고 : https://blog.naver.com/uee8351773/224088896595
'''

N, B = map(str,input().split())    # 변환할 문자값과 해당 문자값의 진수값 입력
print(int(N, int(B)))              # 10진수로 변환(진수변환 문법 사용)
