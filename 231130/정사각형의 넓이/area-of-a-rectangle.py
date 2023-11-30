def solution():
    # 사각형의 한 변 값을 입력받는다.
    side = int(input()) 
    
    result = side**2
    print(result)

    if (side < 5):
        print("tiny")

solution()