def solution():
    # input: 3
    n = int(input()) # 3

    # Iteration 1 ~ input+1
    i = 1
    while i < n+1:
        str_i = str(i)
        pos = len(str_i) - 1
        first_digit = str_i[pos]
        if first_digit == '3' or first_digit == '6' or first_digit == '9':
            print(0, end = ' ')
            i += 1
            continue
        print(i, end = ' ')
        i += 1

solution()