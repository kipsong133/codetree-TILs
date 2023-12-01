def solution():
    # Input: 8 -5 10
    input_arr = list(input().split(" "))
    a = int(input_arr[0])
    b = int(input_arr[1])
    c = int(input_arr[2])

    minimum = a
    for num in [a, b, c]:
        if minimum > num:
            minimum = num
    print(minimum)


solution()