def solution():
    # input: 8
    n = int(input()) # 8

    for i in range(1, n+1):
        if i % 2 == 0 or i % 3 == 0:
            print(1, end = ' ')
        else:
            print(0, end = ' ')


solution()