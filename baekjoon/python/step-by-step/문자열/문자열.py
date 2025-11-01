count = int(input())    # 사용자로부터 입력받을 횟수 입력

# 입력받은 횟수만큼 문자열 입력
for i in range(0,count):
    word = str(input())    # 문자열 입력
    start = word[0]        # 첫 글자를 'start'변수에 저장
    end = int(len(word))-1    # 끝 글자의 주소 계산
    end = word[end]        # 문자열의 끝 글자를 'end'변수에 저장
    print(start + end)      # 공백없이 첫 글자, 끝 글자 출력


'''
위에 주석을 추가하다가 더 간단한 해결법이 생각나서 추가로 기재합니다.

count = int(input())

for i in range(0,count):
    word = str(input())
    print(word[:1] + word[-1])   # 문자열의 인덱스 1번째 미만 자리값 출력, 문자열의 역으로부터 첫 번째 값 출력
'''
