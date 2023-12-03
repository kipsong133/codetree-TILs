def solution():
    # input: 22 31
    input_arr = list(map(int, input().split()))
    a = input_arr[0] # 22
    b = input_arr[1] # 31

    # print out 31 -> 22, i -= 1
    maximum = a if a > b else b
    minimum = a if a < b else b

    for i in range(maximum, minimum - 1, -1):
        print(i, end = ' ')


solution()