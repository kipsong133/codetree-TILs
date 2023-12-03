def solution():
    input_arr = list(map(int, input().split()))
    a = input_arr[1]
    b = input_arr[0]

    # a =< num =< b, odd number
    for i in range(b, a-1, -2):
        print(i, end = " ")



solution()