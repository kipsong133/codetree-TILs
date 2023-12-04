def solution():
    # input: 4
    n = int(input())

    for _ in range(2):
        for _ in range(n):
            for _ in range(n):
                print('*', end = '')
            print('')
        print('')

solution()