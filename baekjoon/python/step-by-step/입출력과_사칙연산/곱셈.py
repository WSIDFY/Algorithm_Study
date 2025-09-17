'''
- 처음 주어지는 수 중 곱해지는 수를 리스트로 받고 
  각 인덱스별로 곱셈 당하는 수와 곱하는 연산 수행
- join(<리스트>)함수를 사용하여 리스트를 문자열로 변환 -> 정수로 바꾸고 마지막 총 곰셈연산 수행
'''
A = int(input())
B = list(input())

num1 = A*int(B[2])
num2 = A*int(B[1])
num3 = A*int(B[0])

trans = (''.join(B))    # 사이에 아무 구분자 없이 B리스트를 연속된 문자열로 변환
num4 = A*int(trans)

print(num1)
print(num2)
print(num3)
print(num4)
