def solution():
    # input: 4 2
    input_arr = list(map(int, input().split()))
    line_count = input_arr[0] # 4줄
    star_count = input_arr[1] # 2개 한줄당

    for _ in range(line_count):
        for _ in range(star_count):
            print('*', end = ' ')
        print('')


solution()