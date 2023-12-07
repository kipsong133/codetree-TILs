def solution():
    # Input: 4
    n = int(input())

    # i: * ' '
    # 0: 8, 0
    # 1: 6, 2
    # 2: 4, 4
    # 3: 2, 6
    # * : ((n * 2) - 2 * i) 개
    # ' ': (2 * i) 개

    # Iteration: lines
    for line in range(n, 0, -1):
        # Iteration: star
        for star in range(line):
            print('*', end = '')
        
        # Iteration: space
        for space in range(n * 2 - (2 * line)):
            print(' ', end = '')

        # Iteration: star
        for star in range(line):
            print('*', end = '')
        
        print('')
    
solution()