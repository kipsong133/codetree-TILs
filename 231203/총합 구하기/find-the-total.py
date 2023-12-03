def solution():
    # input: 15 30
    input_arr = list(map(int, input().split()))

    # sorting
    input_arr.sort()
    a = input_arr[0]
    b = input_arr[1]

    sum_val = 0
    # multiple of 6, not multiple of 8
    # Iteration: a ~ b
    for num in range(a, b+1):
        if num % 6 == 0 and num % 8 != 0:
            sum_val += num
    print(sum_val)

solution()