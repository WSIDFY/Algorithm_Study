sentence = 'the early bird catches the worm.' # 문장제시
conversion = sentence.lower()  # 모든 문장 소문자로 변환

print(conversion[0].upper() + conversion[1:])   # 출력

# 해당 방법 외에도 'capitalize()'함수를 사용하면 첫 글자는 대문자로, 나머지는 소문자로 변경 가능
