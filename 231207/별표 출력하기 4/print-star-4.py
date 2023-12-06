def solution():
    # input: 2
    n = int(input())

    # decreasing stars count
    for i in range(n): # 0, 1, 2, 3 ...
        stars = '* ' * (n - i)
        print(stars)

    # need to iterate just one time.
    for i in range(1, n):
        stars = '* ' * (i + 1)
        print(stars)

solution()