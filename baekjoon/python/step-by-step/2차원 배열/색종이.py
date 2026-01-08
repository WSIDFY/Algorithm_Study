'''
'면적이 겹치는 부분을 어떻게 구하느냐'가 관건인 문제(세로:col, 가로:row)
1. 우선 0으로 크기 100인 도화지 2차원 리스트(canvas)를 만들고
2. 색종이의 개수인 num을 입력받고
3. 색종이의 좌표값 입력받기(canvas의 해당 영역을 'x'로 표기)
-> if문으로 만약 입력받은 좌표값이 기존 좌표값이 'x'인 영역을 포함한다면(영역 계산해야함)
'''
canvas = [0]         # 도화지 2차원 리스트

for canvas_x in range(1, 101):
    for canvas_y in range(1, 101):
        canvas[canvas_x][canvas_y].append(0)

print(canvas)

num = int(input())      # 색종이 갯수 입력

for i in range(num):
    x, y = map(int,input().spilt(' '))

# 풀이 중...
