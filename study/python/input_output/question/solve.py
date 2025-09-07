# report : 주차별 보고서의 '내용'
# report_file : 주차별 보고서 파일을 다루는 '객체'
# week_report : 사용자로 부터 입력받은 보고서의 '파일명'

for week in range(1,51):        # 주차별 보고서 파일 생성 반복문(1주차~50주차까지 반복)

    report_file = open(str(week)+"주차.txt", "w", encoding="utf8")  # 1~50주차 보고서 파일을 저장(텍스트)
    report = ("- " + str(week) + "주차 주간보고 -\n" + "부서 : \n" + "이름 : \n" + "업무 요약 : \n")    # 파일별 내용 생성

    report_file.write(report)  # 보고서 내용을 보고서 파일에 저장
    report_file.close()     # 파일 닫기


week_report = input("몇 주차 보고서를 읽어올까요? : ")  # 불러올 파일명 입력(week_report)

# 사용자로부터 입력받은 파일명이 '.txt'로 끝나지 않는다면 자동으로 붙여주는 if문
if not week_report.endswith(".txt"):
    week_report += ".txt"

# 입력받은 파일명으로 텍스트 모드로 파일 내용을 불러오는 report_file 생성
report_file = open(week_report, "r", encoding="utf8")     
print(report_file.read())   # 입력받은 파일의 전체 내용 출력
report_file.close()     # 파일 닫기
