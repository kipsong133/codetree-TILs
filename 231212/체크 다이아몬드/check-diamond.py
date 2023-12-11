def solution():
    # Input: 4
    n = int(input()) 

    # Iteration: Increasing
    for i in range(n):
        is_star: bool = True
        total = n + i
        front = (n - 1) - i
        remain = total - front # 2*i + 1

        for spacer in range(front):
            print(' ', end = '')
        
        # Contents
        for content in range(remain):
            if is_star:
                print('*', end = '')
                is_star = False
            else:
                print(' ', end = '')
                is_star = True
        is_star = True
        print('')

    m: int = n - 1
    # Iteration: Decreasing
    for i in range(m):
        front = i + 1
        total = 2 * m - i
        remain = total - front
        is_star: bool = True

        # Spacer
        for _ in range(front):
            print(' ', end = '')
        
        # Contents
        for _ in range(remain):
            if is_star:
                print('*', end = '')
                is_star = False
            else:
                print(' ', end = '')
                is_star = True
        print('')


solution()