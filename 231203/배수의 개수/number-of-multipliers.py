def solution():
    # input: 7 42 10 54 34 55 57 60 30 50
    input_arr = [int(input()) for _ in range(10)]

    cnt_3 = 0 # 5
    cnt_5 = 0 # 5
    # print (multiple 3 and 5)'s count
    for num in input_arr:
        if num % 3 == 0:
            cnt_3 += 1
        if num % 5 == 0:
            cnt_5 += 1
    print(f'{cnt_3} {cnt_5}')
        

solution()