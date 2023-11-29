def solution():
    input_values = input().split(" ")
    first_value = int(input_values[0])  # 가로
    second_value = int(input_values[1]) # 세로
    first_value += 8
    second_value *= 3
    print(first_value)
    print(second_value)
    print(first_value * second_value)

solution()