def solution():
    # input: 2 5
    input_arr = list(map(int, input().split()))
    a = input_arr[0]
    b = input_arr[1]

    sum_even = 0
    # Iteration: a ~ b
    for num in range(a, b + 1):
        sum_even += num
    print(sum_even)


solution()