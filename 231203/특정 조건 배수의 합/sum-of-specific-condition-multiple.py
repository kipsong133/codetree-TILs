def solution():
    # input: 13 50
    input_arr = list(map(int, input().split()))
    a = input_arr[0]
    b = input_arr[1]

    sum_val = 0
    # Iteration: a ~ b
    for num in range(a, b + 1):
        if num % 5 == 0:
            sum_val += num

    print(sum_val)

solution()