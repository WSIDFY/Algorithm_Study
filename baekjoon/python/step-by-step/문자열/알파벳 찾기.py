# 알파벳 문자 리스트 생성
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

S = str(input())    # 문자열 입력받기

for i in range(len(alphabet)):      # 알파벳 총 개수만큼 알파벳 포함여부 확인 후 출력
    print(S.find(alphabet[i]),end=' ')      # find()함수는 없으면 자동으로 '-1'반환

'''
아스키코드 방법이 생각이 안 나서 멍청하게 접근했던 문제..
아래는 아스키 코드를 활용한 풀이법이다.

S = input()

for i in range(26):
    print(S.find(chr(ord('a') + i)), end=' ')

1. a(첫 번째)를 찾는다고 할 때 ord('a') + i로 a문자에 대한 아스키 코드97을 반환
2. chr(97)을 통해 문자 a를 'S'문자열에서 탐색 후 인덱스값 반환(없으면 '-1'반환)
'''
