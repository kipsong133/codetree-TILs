def solution():
    # input: 2 13
    input_arr = list(map(int, input().split()))
    a = input_arr[0] # 2
    b = input_arr[1] # 13

    # Condition
    # i is odd, i * 2
    # i is even, i + 3
    while a < b+1:
        print(a, end = ' ')
        if a % 2 == 1:
            a *= 2
            continue
        a += 3
        

solution()