url = "http://naver.com"        # 사이트 주소 설정

# 모든주소가 공통적으로 http://과 .이후의 3자리를 가지기 때문에 해당 범위 제거
value = url[7:-4]   
# 문자형으로 변환 후 남은 글자의 첫 3글자 + 모든 글자 수 + 'e'의 개수 + '!'
password = str(value[:3]) + str(len(value)) + str(value.count('e')) + '!'
# 출력
print('{0}의 비밀번호는 {1}입니다.'.format(url, password))
