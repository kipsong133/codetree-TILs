def solution():
    input_arr = list(map(int, input().split()))
    a = input_arr[0]
    b = input_arr[1]

    # b ~ a step: -1
    for i in range(b, a-1, -1):
        print(i, end = " ")

solution()