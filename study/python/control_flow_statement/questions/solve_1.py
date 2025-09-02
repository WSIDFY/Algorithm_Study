# 현재 풀이중입니다.



from random import *

time = list(range(5,51))      # 5에서 50까지의 리스트 생성
client = [50]             # 고객수 50명 설정
num = 1                 # 고객 카운트 변수

random_time = shuffle(time)     # 5~50 리스트 무작위로 섞기

for i in client:       # 고객 수 만큼 반복

    if 5 <= random_time[i] <= 15:
        print('[0] {0}번째 손님 (소요시간 : {1}분)'.format(num, random_time[i]))
        num += 1

    else:
        print('[ ] {0}번째 손님 (소요시간 : {1}분)'.format(num, random_time[i]))
        num += 1

