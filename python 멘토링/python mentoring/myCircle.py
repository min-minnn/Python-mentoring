"""
get_area(length): 정사각형의 속성을 계산하는 모듈
"""

import math #표준 라이브러리 math 불러오기

PI = math.pi #PI 설정
xpos, ypos = 0, 0 #초기 위치

def get_area(radius): #원의 넓이 구하기
    return (PI * radius**2)

def get_peri(radius): #원의 둘레 계산
    return (2 * PI * radius)

def set_pos(x, y): #위치 설정
    global xpos, ypos
    xpos, ypos = x, y