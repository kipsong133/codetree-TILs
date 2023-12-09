def solution():
    # Input: 2
    n = int(input())
    # i  '*'
    # 0   3
    # 1   1
    # 2   3
    #   (n + 1) - (2 * i)

    for line in range(n):
        # Iteration: Space
        for space in range(2 * line):
            print(' ', end = '')

        # Iteration 1: Decreasing
        for star in range((2 * n - 1) - (2 * line)):
            print('*', end = ' ')
        print('')

    for line in range(n - 1):
        # Iteration: Space
        for space in range(((2 * n - 4)) - (2 * line)):
            print(' ', end = '')

        # Iteration 2: Incresing
        for star in range(2 * line + 3):
            print('*', end = ' ')

        print('')


        

solution()


# 2, 3
# 3, 5
# 4, 7