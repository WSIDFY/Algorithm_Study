word = list(input())        # 입력받을 문자열을 리스트로 저장
word_reverse = word[::-1]   # 입력받은 문자열을 역정렬 후 저장

if word == word_reverse:    # 역정렬된 리스트와 원본 리스트의 값이 동일하다면?
    print(1)
else:
    print(0)
