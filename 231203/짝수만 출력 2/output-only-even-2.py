def solution():
    # input
    input_arr = list(map(int, input().split()))
    b = input_arr[0]
    a = input_arr[1]

    # print out even number, a =< number =< b
    # start point
    i = b
    while i > a-1:
        if i % 2 == 0:
            print(i, end = " ")
        i -= 1
solution()