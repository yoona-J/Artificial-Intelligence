import turtle
import numpy as np

# x, y 위치에 pSize 크기의 픽셀을 pCol 색으로 그리는 함수
def putPixel(x, y, pSize, pCol):
    turtle.penup()                              # 펜 기능 비활성화 - 좌표 이동
    turtle.goto(x * pSize, (-1) * y * pSize)    # 주어진 좌표로 이동
    turtle.pendown()                            # 펜 기능 활성화
    turtle.begin_fill()                         # 다각형 내부 채우기
    turtle.fillcolor(pCol)                      # 다각형 채움색 설정
    turtle.setheading(45)                       # 시작 각도 설정 - 45도
    turtle.circle(pSize / 2, steps=4)           # 정사각형 픽셀 나타내기
    turtle.end_fill()                           # 채우기 끝

# 데이터셋
myImg = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 1, 1, 0, 0, 0, 0],
                  [1, 1, 1, 1, 1, 0, 0, 0],
                  [1, 1, 1, 1, 1, 0, 0, 0],
                  [0, 1, 1, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]])

# pixel 사이즈 반지름
pixelSize = 30

# 이미지의 행벡터(Xj) range
for j in range(0, 8):
    # Xj 내 Xji roop
    for i in range(0, 8):
        # Xji 값 확인 후 0보다 크면
        if myImg[j][i] > 0:
            # 오렌지색
            putPixel(i, j, pixelSize, "orange")
        # Xji 값 확인 후 0보다 같거나 작으면
        else:
            # 흰색
            putPixel(i, j, pixelSize, "white")