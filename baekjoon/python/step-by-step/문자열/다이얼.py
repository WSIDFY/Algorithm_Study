number = {
    'W':10,'X':10,'Y':10,'Z':10,
    'T':9,'U':9,'V':9,
    'P':8,'Q':8,'R':8,'S':8,
    'M':7,'N':7,'O':7,
    'J':6,'K':6,'L':6,
    'G':5,'H':5,'I':5,
    'D':4,'E':4,'F':4,
    'A':3,'B':3,'C':3
}

value = str(input())
time = 0

for i in range(len(value)):
    time += number.get(value[i])    # 입력받은 문자열의 첫 글자부터 number사전에 있는 값이면 value값(시간)을 불러와 time에 더하기

print(time)

'''
딕셔너리를 잘 활용하지 않아 단순 박복문으로 문자열의 각 자리를 비교하려고 접근했던 문제였으나
dict + get() 방식으로 쉽게 해결 가능
'''
