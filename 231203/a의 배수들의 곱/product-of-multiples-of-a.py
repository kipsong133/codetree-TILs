def solution():
    # input: 4, 10
    input_arr = list(map(int, input().split()))
    a = input_arr[0]
    b = input_arr[1]

    result = 1
    # Iteration: 1 ~ b
    for num in range(1, b+1):
        if num % a == 0:
            result *= num
    print(result)


solution()