def solution():
    # input: 2
    n = int(input())

    # line count
    for i in range(n):
        star_count = n - (n - i)

        # star count
        # n - (n - i) : 최대갯수 - (최대갯수 - 현재 인덱스)
        for _ in range(star_count + 1):
            print('*', end = ' ')
        print('')
            

solution()