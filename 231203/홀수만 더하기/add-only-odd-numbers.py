def solution():
    # input: 5
    n = int(input())

    # input: 5 2 7 3 9 4
    input_arr = list(int(input()) for _ in range(n))

    sum_val = 0
    # Iteration: input_arr
    for num in input_arr:
        if num % 2 == 1 and num % 3 == 0:
            sum_val += num
    print(sum_val)

solution()