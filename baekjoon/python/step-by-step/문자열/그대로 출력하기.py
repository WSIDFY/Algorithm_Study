'''
keyword_list = []

for i in range(0,100):
    keyword = input()

    if (keyword[0] or keyword[-1]) == ' ':
        break
    else:
        keyword_list.append(keyword)
        continue

for j in range(len(keyword_list)):
    print(keyword_list[j],end='\n')

- 위의 코드처럼 문자의 앞이나 뒤에 공백이 있을 때 에러로 치고 앞전 문자열까지만 출력하는 형태로 접근했었다.
- 종료 기준에 대한 이해도가 부족하여 접근이 어려웠던 문제였던 것 같다.
'''

import sys

while True:     # 오류가 없을 시 계속해서 반복

    try: 
        word = sys.stdin.readline()     # 한 줄씩 입력받고 word에 임시저장

        if word == "":      # 만약 입력받은 문자열 없이 \n으로만 끝난다면?
            break           # 중지
        else:               # 혹은(문자열이 정상적으로 입렫되었을 때)
            print(word,end='')      # 출력  
        
    except EOFError:        # 에러 대비 except문
        break

