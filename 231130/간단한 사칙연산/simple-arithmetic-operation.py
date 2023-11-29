def solution():
    input_values = input().split(" ")
    a = int(input_values[0])
    b = int(input_values[1])

    result_sum = a + b
    result_minus = a - b
    result_divi = a / b
    result_left = a % b
    print(result_sum)
    print(result_minus)
    print(int(result_divi))
    print(result_left)


solution()