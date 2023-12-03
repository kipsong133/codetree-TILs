def solution():
    # 몇 개 입력받을 지 정수
    n = int(input()) # 5 개를 입력받겠다.
    
    # input: 2 7 3 9 4 (각각 줄바꿈) 그래서 5 개를 입력 받았다.
    input_arr = [int(input()) for _ in range(n)]
    for num in input_arr:
        if num % 2 == 1 and num % 3 == 0:
            print(num)
            
solution()