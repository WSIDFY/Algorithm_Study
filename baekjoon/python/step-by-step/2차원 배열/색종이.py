'''
리스트 컴프리헨션 방식 숙지해두기!!
ex.) canvas = [[0 for _ in range(100)] for _ in range(100)]

즉 0으로 채워진 100X100의 2차원 리스트를 만들고 입력받은 좌표값의 x,y에 각각 10만큼 반복해서 1로 채운 뒤에
원래 1인 자리는 넘어가는 형식으로 해서 검정종이 영역을 1로 칠하고 마지막에 for문으로 공간의 값이 1인 곳만 count진행
[
[0,0,0,0,0,. . .]
[0,0,0,0,0...]
]
'''
# 0으로 채워진 100X100크기의 2차원 리스트 생성(리스트 컴프리헨션 방식)
canvas = [[0 for _ in range(100)] for _ in range(100)]

# 색종이의 개수 입력받기
num = int(input())      # 색종이 갯수 입력

# 입력받은 개수 만큼 색종이의 좌표 입력받기
for z in range(num):
    x, y = map(int,input().split())      # 열, 행 순서로 입력받음

    for a in range(10):                  # a값을 10까지 증가시킴
        for b in range(10):              # b값을 10까지 증가시킴
            if canvas[x+a][y+b] == 0:    # 행과 열의 좌표를 1씩 10크기만큼 증가시키면서 0인 값을 1로 바꾸기
                canvas[x+a][y+b] = 1
            else:                        # 이미 1이라면(겹치는 부분)패스
                continue

width = 0                                # 전체 너비값을 저장할 변수
# 1로 채워진 공간의 개수 연산
for x_line in range(100):
    for y_line in range(100):
        if canvas[x_line][y_line] == 1:   # 전체 기준 각각의 위치에 1인 값이 있다면
            width += 1                    # width + 1

print(width)

'''
(참고한 내용)
- 리스트 컴프리헨션 부분
'''
