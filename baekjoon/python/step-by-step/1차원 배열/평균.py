score = []    # 실제 점수 입력받을 리스트
fake_score = 0    # 가짜 점수들의 합을 저장할 변수

count = int(input())    # 과목 수 입력
score = list(map(int, input().split(' ')))    # score 리스트에 과목 점수 넣기

high_score = max(score)    # 최고 점수 구하기

# 과목 수 만큼 각 과목별로 점수 조작 후 fake_score변수에 더하기
for i in range(0,count):
    value = score[i]/(high_score*100)
    fake_score += value

average = fake_score / count    # 합산된 가짜점수 나누기 과목 수로 평균 산출

print(average*10000)      # 출력 형식 지정후 출력
