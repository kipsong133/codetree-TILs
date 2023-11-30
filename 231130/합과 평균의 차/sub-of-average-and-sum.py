def solution():
    input_arr = list(map(int, input().split(" ")))
    a = input_arr[0]
    b = input_arr[1]
    c = input_arr[2]

    result_sum = sum(input_arr)
    result_avg = result_sum / len(input_arr)
    result = result_sum - result_avg
    print(result_sum)
    print(int(result_avg))
    print(int(result))

solution()