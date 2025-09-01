# sample() : 리스트에서 원하는 개수만큼 중복 없이 값을 뽑는 동작을 수행
# shuffle() : 리스트의 데이터를 무작위로 섞어주는 동작을 수행

from random import *  # 랜덤모듈 적용

draw = list(range(1,21))       # 1~20까지의 리스트 생성
shuffle(draw)                  # 리스트 무작위 섞기

chiken_winner = sample(draw, 1)[0]      # 치킨 당첨자를 1명 뽑고 첫 번째 인덱스의 '값'형태로 추출
draw.remove(chiken_winner)              # 리스트에서 치킨 당첨자 숫자를 제거
coffee_winner = sample(draw, 3)         # 치킨 당첨자가 제거된 리스트에서 3명 추출


# 출력된 리스트를 str형으로변환 후 출력
print('-- 당첨자 발표 --\n' + '치킨 당첨자 : ' + str(chiken_winner) + '\n' + 
      '커피 당첨자 : ' + str(coffee_winner) + '\n' + 
      '-- 축하합니다! --')
