def solution():
    # Input: 1, 2, 3
    input_arr = list(map(int, input().split(" ")))

    a = input_arr[0] # 1
    b = input_arr[1] # 2
    c = input_arr[2] # 3

    is_satisfied = (a < b) and (b < c)
    print(1 if is_satisfied else 0)



solution()