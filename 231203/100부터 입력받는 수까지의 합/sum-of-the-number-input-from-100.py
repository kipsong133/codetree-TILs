def solution():
    # input: 91
    n = int(input())

    sum_val = 0
    # Iteration: n ~ 100
    for num in range(n, 101):
        sum_val += num
    print(sum_val)


solution()