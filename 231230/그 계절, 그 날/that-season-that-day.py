def isYoon(Y):
    leap_Y = False   # 윤년인지 아닌지 체크할 변수로 기본 평년으로 체크
    if Y % 4 == 0:               # 4로 나누어떨어지는지 확인
        if Y % 100 == 0:         # 100으로 나누어떨어지는지 확인
            if Y % 400 == 0:     # 400으로 나누어떨어지는지 확인
                leap_Y = True    # 4, 100, 400으로 나누어떨어지면 윤년
        else:
            leap_Y = True # 4로 나누어떨어지고, 100으로 나누어떨어지지 않으면 윤년

    return leap_Y
def noDay(Y,M,D):
    if (M==4 or M==6 or M==9 or M==11) and D>30:
        return True
    elif M==2 and isYoon(Y)==False and D>28:
        
        return True
    elif M==2 and isYoon(Y)==True and D>29:
        
        return True
    else:
        return False
def solution(Y,M,D):
    if noDay(Y,M,D)==True: #존재하지않으면 return -1
        return -1
    elif 3<=M<=5:
        return "Spring"
    elif 6<=M<=8:
        return "Summer"
    elif 9<=M<=11:
        return "Fall"
    elif M==12 or 1<=M<=2:
        return "Winter"

#입력
Y, M, D= map(int, input().split())
print(solution(Y,M,D))