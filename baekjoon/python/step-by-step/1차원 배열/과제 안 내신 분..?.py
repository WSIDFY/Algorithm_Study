student_num=[]  #과제 제출한 학생을 저장할 리스트
imposter=[]  # 과제 제출을 하지 않은 학생을 저장할 리스트

# 과제 제출한 28명의 학생 번호를 입력받고 student_num리스트에 저장
for i in range(0,28):
    N = int(input())
    student_num.append(N)

# student_num에 들어가있는 과제를 제출한 학생들 중에 1번~30번 범위에 없는(제출하지 않은)학생을 찾고 imposter리스트에 저장 
for i in range(1,31):
    if i in student_num:  # student_num에 들어가있다면 넘어가기
        continue
    else:                 # student_num에 없으면 imposter에 저장
        imposter.append(i)

imposter.sort()           # 리스트 오름차순 정렬

# imposter리스트에 있는 요소들을 개행 단위로 하나씩 출력
for i in range(0, len(imposter)):
    print(imposter[i], end='\n')
