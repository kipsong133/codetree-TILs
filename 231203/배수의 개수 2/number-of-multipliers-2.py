def solution():
    # input: 1, 2, 3 ...
    input_arr = list(int(input()) for _ in range(10))

    cnt = 0
    # print out odd number count
    for num in input_arr:
        if num % 2 == 1:
            cnt += 1
    print(cnt)

solution()