def solution():
    # input: 40
    a = int(input())

    # Iteration: 1 ~ a
    for num in range(1, a+1):
        # even number, not multiple of 4
        if num % 2 == 0 and num % 4 != 0:
            continue

        # even number, quotient divided by 8
        quot_8 = int(num / 8)
        if quot_8 % 2 == 0:
            continue

        # number < 4, remainder divided by 7
        remainder_7 = num % 7
        if remainder_7 < 4:
            continue

        print(num, end = ' ')

solution()