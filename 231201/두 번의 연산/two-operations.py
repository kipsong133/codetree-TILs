def solution():
    input_num = int(input())

    # Condition: odd number
    if input_num % 2 == 1:
        input_num += 3
    
    if input_num % 3 == 0:
        input_num /= 3

    print(int(input_num))

solution()