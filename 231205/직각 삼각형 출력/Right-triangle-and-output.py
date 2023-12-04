def solution():
    # input: 5
    n = int(input())

    # line count: n
    for i in range(n):
        # star count
        star_count = n - (n - i * 2) + 1
        stars = '*' * star_count 
        print(stars)

solution()