def solution():
    # Input: 4
    n = int(input())

    # Iteration 1: increasing 
    for i in range(1, n + 1):
        stars = '*' * i
        print(stars)
        print()

    # Iteration 2: Decreasing
    for i in range(1, n):
        stars = '*' * (n - i)
        print(stars)
        print()

solution()