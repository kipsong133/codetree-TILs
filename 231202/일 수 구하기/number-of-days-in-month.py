def solution():
    # Input: 1 
    # - month
    month = int(input())

    # 2 = 28days
    if (month == 2):
        print(28)
        return

    # remainder: 1, 3, 4, 5, 6, 7, 8, 9, 10, 11
    # 1, 3, 5,7,8,10,12 = 31days
    # 4, 6, 9, 11 = 30days

    if month < 8:
        # 1, 3, 4, 5, 6, 7
        if month % 2 == 1:
            # 1, 3, 5, 8
            print(31)

        else: 
            # 4, 6
            print(30)

    if month >= 8:
        # 8, 9, 10, 11, 12
        if month % 2 == 1:
            # 9, 11
            print(30)
        else:
            # 8, 10, 12
            print(31)

solution()