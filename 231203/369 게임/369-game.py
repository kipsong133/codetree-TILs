def solution():
    # input: 3
    n = int(input()) # 3

    # Iteration 1 ~ input+1
    i = 1
    while i < n+1:
        str_i = str(i)
        if str_i[0] == '3' or str_i[0] == '6' or str_i[0] == '9':
            print(0, end = ' ')
            i += 1
            continue
        print(i, end = ' ')
        i += 1

solution()