def solution():
    # Input: 2
    n = int(input())

    # Iteration: increasing
    for i in range(n):
        # spacer
        for _ in range(n - 1 - i):
            print(' ', end = '')
        
        # star
        for _ in range(2 * i + 1):
            print('*', end = '')
        print('')

    # Iteration: Decreasing
    for i in range(n-1, 0, -1):
        # spacer
        for _ in range(n - i):
            print(' ', end = '')

        # star
        for _ in range(2 * i - 1):
            print('*', end = '')
        print('')


solution()