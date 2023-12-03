def solution():
    # input
    n = int(input())

    # mutiple of 3
    i = 1
    while i < n+1:
        if i % 3 == 0:
            print(i, end = " ") 
        i += 1

solution()