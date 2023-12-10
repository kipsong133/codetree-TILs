def solution():
    # Input: 3
    n = int(input())

    # Iteration: Increasing
    for i in range(n):
        # Spacer
        for spacer in range((n - 1) - i):
            print('  ', end = '')
        
        # Content
        for content in range((i + 1)):
            print('@', end = ' ')
        print('')

    # Iteration: Decreasing
    for i in range(n - 1):
        # Contents
        for content in range((n - 1) - i):
            print('@', end = ' ')
        print('')

    
solution()