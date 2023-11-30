def solution():
    input_arr = list(map(int, input().split(" ")))
    a = input_arr[0]
    b = input_arr[1]
    c = input_arr[2]
    result_sum = a + b + c
    result_avg = int(result_sum / 3)
    print(result_sum)
    print(result_avg)

solution()