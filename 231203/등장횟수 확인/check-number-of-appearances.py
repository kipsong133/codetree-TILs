def solution():
    # input: 124 341 547 56 23
    input_arr = [int(input()) for _ in range(5)]

    cnt_even = 0
    for num in input_arr:
        if num % 2 == 0:
            cnt_even += 1
    print(cnt_even)

solution()