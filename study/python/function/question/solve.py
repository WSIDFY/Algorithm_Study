avg_weight = 0    # 평균 몸무게 변수

# 두 개의 전달값으로 평균 몸무게를 계산하는 함수
def std_weight(height, gender):
    
    global avg_weight # 함수 내에서 전역변수 사용 선언

    # 남자일 때 평균 몸무게 연산
    if gender == '남자': 
      avg_weight = height*height*22
      return round(avg_weight, 2) # 소수점 2자리 까지만 전달
    
    # 남자가 아닐 때(여자일 때)평균 몸무게 연산
    else:
      avg_weight = height*height*21
      return round(avg_weight, 2)

gender = '남자'
height = 1.76

# 키를 m단위로 받았기 때문에 출력할 때는 100을 곱한 후 정수형으로 변환
print('키 {0}cm {1}의 표준 체중은 {2}kg입니다.'
      .format(int(height*100), gender, std_weight(height, gender)))
