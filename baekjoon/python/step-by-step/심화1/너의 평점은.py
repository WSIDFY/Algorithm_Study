'''
1. 우선 등급에 따른 과목 평점을 dict으로 정의
2. 20번 반복해서 과목명/학점/등급을 입력받고 score_list에 저장 
3. score_list에 있는 즉, 입력받은 정보 중 '학점' * '내가 받은 등급과 매칭되는 과목평점'을 해서 나온값을
과목별로 모두 구하고 다 더함
4. 3에서 더해진 값을 학점(내가 받은)의 총합으로 나눈 값을 구하기
5. 단 P등급의 과목이라면 무시하고 넘어가야함
'''


# 등급에 따른 과목의 평점
lecture_dict = {'A+':4.5, 'A0':4.0, 'B+':3.5, 
                'B0':3.0, 'C+':2.5, 'C0':2.0, 
                'D+':1.5, 'D0':1.0, 'F':0.0}

# input_list=[]
score_list=[]   # 학점을 저장할 리스트
rating_list=[]  # 등급을 저장할 리스트

# 20번 만큼 입력 반복
for i in range(0,20):
    input_list = list(map(str, input().split(' ')))     # 한 과목을 입력받고 반복해서 지워지는 임시공간
    
    if input_list[2] == 'P':
        input_list=[]
        continue

    score_list.append(input_list[1])        # 입력받은 과목의 학점을 저장
    rating_list.append(lecture_dict.get(input_list[2]))       # 입력받은 과목의 등급을 과목평점과 매칭해서 해당 평점을 저장
    input_list=[]       # 입력받은 리스트 초기화

float_score_list = [float(num) for num in score_list]       # 입력받은 문자 리스트를 실수 리스트로 변환

total=0
# 학점의 총합 구하기
for j in range(len(score_list)):
    total += float_score_list[j]       # 문자로 들어가있으니까 정수로 변환 후 total변수에 더하면서 저장

mul=0
sum=0
# 전공과목별 학점*과목평점의 합 구하기
for z in range(len(score_list)):
    mul = float_score_list[z]*rating_list[z]
    sum += mul

print(round((sum/total),6))

'''
(참고한 내용)
- 입력받은 값이 사전에 있는지 탐색하는 로직(get)
- 입력받은 문자를 리스트에 정수로 저장하는 로직(float_score_list = [float(num) for num in score_list])
- 리스트에 있는 값이 정수 형태의 문자열이면 int()로 변환이 가능! (즉, 3.0과 같은 실수형은 안됨)
'''
