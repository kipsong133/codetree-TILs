def solution():
    # Input: 5
    n = int(input())
    
    # Iteration: line
    for line in range(n * 2):
        # Iteration: spacing
        for space in range(line):
            print('  ', end = '')

        # Iteration 2: star
        for j in range((n * 2) - 2 * line - 1):
            print('* ', end = '')
        print()
solution()