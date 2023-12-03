def solution():
    # input: 12
    n = int(input()) # 12

    # Iteration 1 ~ input+1
    n_index = 1
    while n_index < n+1:
        str_n = str(n)
        if len(str_n) == 1:
            if n_index == 3 or n_index == 6 or n_index == 9:
                print(0)
                n_index += 1
                continue

        # Iteration str_n
        for i in range(0, len(str_n) - 1):
            digit_str = str_n[i]
            if digit_str == '3' or digit_str == '6' or digit_str == '9':
                # Condition: has '3', '6' ,'9'
                print(0, end = ' ')
                n_index += 1
                continue
        print(n_index, end = ' ')
        n_index += 1


solution()