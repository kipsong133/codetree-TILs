def solution():
    # input: 4
    n = int(input())

    # line count
    for i in range(n):
        
        star_count = (n - i)
        # star count
        for _ in range(star_count): 
            starts = '*' * star_count
            print(starts, end = ' ')

        print('')


solution()