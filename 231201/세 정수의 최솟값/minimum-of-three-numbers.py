def solution():
    # Input: 8 -5 10
    input_arr = list(map(int, input().split(" ")))
    a = input_arr[0]
    b = input_arr[1]
    c = input_arr[2]

    minimum = float("inf")
    for num in input_arr:
        if minimum > num:
            minimum = num
    print(minimum)


solution()