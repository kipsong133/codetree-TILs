def solution():
    # input
    input_arr = list(map(int, input().split()))
    a = input_arr[0]
    b = input_arr[1]

    # print out even number in a ~ b
    # start point
    i = a
    while i < b+1:
        if i % 2 == 0:
            print(i, end = " ")
        i += 1

solution()