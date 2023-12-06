def solution():
    # Input: 3
    n = int(input())

    # Iteration: lines
    for line in range(n):
        # Iteration: spacer
        for space in range(n - line - 1):
            print('  ', end =  '')
        
        # Iteration: stars
        for star in range(2 * line + 1):
            print('*', end = ' ')
        print()

solution()