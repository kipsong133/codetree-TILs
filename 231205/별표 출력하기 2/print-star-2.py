def solution():
    # input: 2
    n = int(input())    

    # line count
    for i in range(n): # 2 line
        # start count
        for _ in range(n - i):
            print('*', end = ' ')
        print('')

solution()