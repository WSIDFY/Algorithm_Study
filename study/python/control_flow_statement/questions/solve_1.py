from random import *

client = range(1,51)    # 총 50명의 승객 리스트 생성
total = 0               # 총 탑승인원을 구하는 변수

for i in client:        # 탑승객 만큼 반복하는 반복문
    time = randrange(5,51)  #5분~50분 사이의 난수를 생성하는 time변수

    if 5 <= time <= 15:   # 조건에 맞는 탑승객일 때
        print('[0] {0}번째 손님 (소요시간 : {1}분)'.format(i, time))
        total += 1    # 총 탑승인원 +1

    else:       # 조건에 맞지 않는 탑승객일 때
        print('[ ] {0}번째 손님 (소요시간 : {1}분)'.format(i, time))

print('총 탑승객 : {}명'.format(total))
