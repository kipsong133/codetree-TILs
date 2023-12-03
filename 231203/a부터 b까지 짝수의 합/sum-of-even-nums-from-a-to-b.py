def solution():
    # input: 2 5
    input_arr = list(map(int, input().split()))

    # sorting
    input_arr.sort()
    a = input_arr[0]
    b = input_arr[1]

    sum_val = 0
    for num in range(a, b+1):
        if num % 2 == 0:
            sum_val += num
    print(sum_val)

solution()