while True:
    try:
        A, B = map(int, input().split(' '))
        print(str(A+B))
    except:
        break

# try, except문을 사용하지 않고 진행하면 런타임 오류발생
# 출력 형식이 정해져있지 않은 문제
