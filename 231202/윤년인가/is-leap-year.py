def solution():
    # Input: 2020 
    # year
    y = int(input())

    # Condition 1: multiple of 4 
    # Condition 2: not multiple of 100
    # Condition 3: multiple of 400
    is_leap_year: bool = False
    if y % 4 == 0:
        is_leap_year = True

    if y % 100 == 0:
        is_leap_year = False
    
    if y % 400 == 0:
        is_leap_year = True
    
    result = str(is_leap_year).lower()
    print(result)

solution()